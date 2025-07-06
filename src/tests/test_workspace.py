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
