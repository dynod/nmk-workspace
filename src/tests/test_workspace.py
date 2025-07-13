import json
import shutil
from pathlib import Path

from nmk.tests.tester import NmkBaseTester
from nmk.utils import run_with_logs


class TestWorkspacePlugin(NmkBaseTester):
    @property
    def templates_root(self) -> Path:
        return Path(__file__).parent / "templates"

    def test_version(self):
        self.nmk(self.prepare_project("ref_workspace.yml"), extra_args=["version"])

    def test_no_subprojects(self):
        self.nmk(self.prepare_project("ref_workspace.yml"), extra_args=["--print", "workspaceSubProjects"])
        self.check_logs('Config dump: { "workspaceSubProjects": [] }')

    def test_with_real_submodules(self):
        # Use git to preare a project with a real submodule
        p = self.prepare_project("ref_workspace.yml")
        run_with_logs(["git", "init"], cwd=self.test_folder)
        run_with_logs(["git", "submodule", "add", "--depth", "1", "https://github.com/dynod/nmk-workspace.git", "some/sub/folder"], cwd=self.test_folder)
        run_with_logs(["git", "submodule", "add", "--depth", "1", "https://github.com/dynod/empty-project.git", "some/empty"], cwd=self.test_folder)

        # Check submodules list
        self.nmk(p, extra_args=["--print", "workspaceSubProjects"])
        self.check_logs(
            [
                "Sub-project some/empty does not have a default nmk model file, skipping it.",
                'Config dump: { "workspaceSubProjects": [ "some/sub/folder" ] }',
            ]
        )

    def run_workspace_task(self, task: str, extra_config: dict = None, expected_rc: int = 0) -> Path:
        sub_projects = ["libs/foo", "tools/bar"]
        for sub_project in sub_projects:
            sub_p_folder = self.test_folder / sub_project
            sub_p_folder.mkdir(parents=True, exist_ok=True)
            shutil.copy(self.template(f"{sub_p_folder.name}.yml"), sub_p_folder / "nmk.yml")

        p = self.prepare_project("ref_workspace.yml")
        whole_extra_config = {"workspaceSubProjects": sub_projects, "workspaceBuildExtraArgs": "--skip setup"}
        if extra_config:
            whole_extra_config.update(extra_config)
        self.nmk(p, extra_args=[task, "--skip", "setup", "--config", json.dumps(whole_extra_config)], expected_rc=expected_rc)

    def test_subprojects_clean(self):
        self.run_workspace_task("clean")

    def test_subprojects_package(self):
        self.run_workspace_task("package")

    def test_subprojects_tests_default(self):
        self.run_workspace_task("tests")

        # Some tests are expected to fail, but without raising an error
        self.check_logs("!! Failed to build sub-project: libs/foo !!")

    def test_subprojects_tests_explode(self):
        self.run_workspace_task("tests", {"workspaceBuildIgnoreFailures": {"tests": False}}, expected_rc=1)

        # Some tests are expected to fail, but without raising an error
        self.check_logs("!! Failed to build sub-project: libs/foo !!")

    def test_subprojects_clean_duplicate(self):
        self.run_workspace_task("clean", {"workspaceSubProjects": ["libs/foo", "libs/foo"]})

    def test_subprojects_clean_exclude(self):
        self.run_workspace_task("clean", {"workspaceSubProjectsToExclude": ["libs/foo"]})
        self.check_logs(">> skipped (excluded)")
