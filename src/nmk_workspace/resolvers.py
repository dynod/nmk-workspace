"""
Nmk workspace plugin config item resolvers.
"""

from pathlib import Path
from subprocess import CompletedProcess
from typing import cast

from nmk.logs import NmkLogger
from nmk.model.resolver import NmkListConfigResolver
from nmk.utils import run_with_logs  # type: ignore


class SubProjectsResolver(NmkListConfigResolver):
    """
    Resolver usable find sub-projects in the workspace tree.

    Default behavior is to look sub-projects by iterating through git submodules.
    (other behaviors may be implemented if needed later).
    """

    def get_value(self, name: str, root: str, only_nmk_projects: bool = True) -> list[str]:  # type: ignore
        """
        Resolver for sub-projects list.

        :param root: root path of the workspace
        :param only_nmk_projects: if True (default), only return sub-projects having a default nmk project file (nmk.yml)
        :return: list of sub-projects paths relative to the workspace root
        """

        # Ask git for submodules paths
        root_path = Path(root)
        cp = cast(
            CompletedProcess[str], run_with_logs(["git", "submodule", "foreach", "--quiet", "--recursive", "echo $sm_path"], cwd=root_path)
        )  # Note that $sm_path is a git variable, meaning this syntax is supported both on Linux and Windows
        nmk_models: list[str] = []
        for candidate in cp.stdout.splitlines(keepends=False):
            # Only keep ones with a default nmk model file
            sub_project_path = candidate.strip()
            candidate_path = root_path / sub_project_path / "nmk.yml"
            if (not only_nmk_projects) or candidate_path.is_file():
                nmk_models.append(sub_project_path)
            else:
                NmkLogger.debug(f"Sub-project {sub_project_path} does not have a default nmk model file, skipping it.")
        return nmk_models
