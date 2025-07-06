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

    def test_filtered_python_subprojects(self):
        # Prepare a sample project with fake nmk sub-projects
        sub_proj1 = "foo/bar"
        sub_proj2 = "foo/baz"
        sub_proj3 = "qux"
        sub_proj4 = "foo/empty"
        for sub_p in [sub_proj1, sub_proj2, sub_proj3, sub_proj4]:
            sub_path = self.test_folder / sub_p
            sub_path.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(self.template(f"{sub_path.name}.yml"), sub_path / "nmk.yml")
        p = self.prepare_project("ref_workspace.yml")

        # Check python sub-modules ordered list
        self.nmk(
            p,
            extra_args=[
                "--print",
                "workspacePythonSubProjects",
                "--config",
                f'{{"workspaceSubProjects": ["{sub_proj1}", "{sub_proj2}", "{sub_proj3}", "{sub_proj4}"]}}',
            ],
        )
        self.check_logs(['Config dump: { "workspacePythonSubProjects": [ "foo/baz", "foo/bar", "qux" ] }'])

    def test_filtered_python_subprojects_cyclic(self):
        # Prepare a sample project with fake nmk sub-projects (and cyclic dependencies)
        sub_proj1 = "foo/bar"
        sub_proj2 = "foo/baz2"
        for sub_p in [sub_proj1, sub_proj2]:
            sub_path = self.test_folder / sub_p
            sub_path.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(self.template(f"{sub_path.name}.yml"), sub_path / "nmk.yml")
        p = self.prepare_project("ref_workspace.yml")

        # Check python sub-modules ordered list
        self.nmk(
            p,
            extra_args=[
                "--print",
                "workspacePythonSubProjects",
                "--config",
                f'{{"workspaceSubProjects": ["{sub_proj1}", "{sub_proj2}"]}}',
            ],
            expected_error="Error occurred while resolving config workspacePythonSubProjects: Cyclic dependency: bar referenced from artifacts bar -> baz",
        )

    def test_corrupted_subprojects(self):
        # Prepare a sample project with fake nmk sub-projects
        sub_proj5 = "foo/corrupted"
        for sub_p in [sub_proj5]:
            sub_path = self.test_folder / sub_p
            sub_path.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(self.template(f"{sub_path.name}.yml"), sub_path / "nmk.yml")
        p = self.prepare_project("ref_workspace.yml")

        # Check python sub-modules ordered list
        self.nmk(
            p,
            extra_args=[
                "--print",
                "workspacePythonSubProjects",
                "--config",
                f'{{"workspaceSubProjects": ["{sub_proj5}"]}}',
            ],
            expected_error="Failed to load sub-project model for foo/corrupted",
        )
