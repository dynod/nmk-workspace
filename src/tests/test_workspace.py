from pathlib import Path

from nmk.tests.tester import NmkBaseTester


class TestWorkspacePlugin(NmkBaseTester):
    @property
    def templates_root(self) -> Path:
        return Path(__file__).parent / "templates"

    def test_version(self):
        self.nmk(self.prepare_project("ref_workspace.yml"), extra_args=["version"])
