"""
Nmk workspace plugin config item resolvers.
"""

import re
from pathlib import Path
from typing import cast

import tomlkit
from nmk.logs import NmkLogger
from nmk.model.resolver import NmkListConfigResolver
from nmk.utils import run_with_logs

# Expected pyproject file
_PY_PROJECT = "pyproject.toml"


class SubProjectsResolver(NmkListConfigResolver):
    """
    Resolver usable find sub-projects in the workspace tree.

    Default behavior is to look sub-projects by iterating through git submodules.
    (other behaviors may be implemented if needed later).
    """

    def get_value(self, name: str, root: str, only_nmk_projects: bool = True, only_python_projects: bool = False, only_basenames: bool = False) -> list[str]:  # type: ignore
        """
        Resolver for sub-projects list.

        :param root: root path of the workspace
        :param only_nmk_projects: if True (default), only return sub-projects having a default nmk project file (nmk.yml)
        :param only_python_projects: if True, only return sub-projects having a Python project file (pyproject.toml)
        :param only_basenames: if True, only return sub-projects basenames (i.e. without their relative parent folders)
        :return: list of sub-projects paths relative to the workspace root
        """

        # Build expected files list
        expected_files: list[str] = [] + (["nmk.yml"] if only_nmk_projects else []) + ([_PY_PROJECT] if only_python_projects else [])  # type: ignore

        # Ask git for submodules paths
        root_path = Path(root)
        cp = run_with_logs(["git", "submodule", "foreach", "--recursive", "echo xxx"], cwd=root_path)
        nmk_models: list[str] = []
        SUB_MODULE_PATTERN = re.compile(r"^.+ \'(.*)\'$")
        for candidate in map(
            lambda x: x.group(1) if x is not None else None,
            filter(lambda x: x is not None, map(lambda x: SUB_MODULE_PATTERN.match(x.strip()), cp.stdout.splitlines(keepends=False))),
        ):
            # Check candidate path is valid and exists
            assert candidate is not None  # for type hinting
            candidate_path = Path(candidate)
            if candidate_path.is_absolute() or not (root_path / candidate_path).exists():  # pragma: no cover
                NmkLogger.debug(f"Sub-project path {candidate_path} is not valid, skipping it.")
                continue

            # Check for expected files, if any
            sub_module_path = candidate_path.name if only_basenames else candidate_path.as_posix()
            if (not expected_files) or all((root_path / candidate_path / file).is_file() for file in expected_files):
                nmk_models.append(sub_module_path)
            else:
                NmkLogger.debug(f"Sub-project {sub_module_path} does not have some of expected files ({', '.join(expected_files)}), skipping it.")
        return nmk_models


class PythonPackagesResolver(NmkListConfigResolver):
    """
    Resolver usable to find Python packages names in the workspace tree.

    Default behavior is to look for sub-projects having a pyproject.toml file and read their package name from it.
    """

    def get_value(self, name: str, root: str, python_subprojects: list[str]) -> list[str]:  # type: ignore
        """
        Resolver for Python packages names list.

        :param root: root path of the workspace
        :param python_subprojects: list of sub-projects paths relative to the workspace root
        :return: list of Python packages names
        """

        # Read package names from pyproject.toml files
        root_path = Path(root)
        package_names: list[str] = []
        for candidate in python_subprojects:
            candidate_project = root_path / candidate / _PY_PROJECT
            if not candidate_project.is_file():  # pragma: no cover -- should not happen since we already filtered python_subprojects, but just in case
                NmkLogger.debug(f"Sub-project {candidate} does not have a pyproject.toml file, skipping it.")
                continue

            # Read name from project file
            tomldoc = tomlkit.parse(candidate_project.read_text())
            toml_project = cast(dict[str, str | None], tomldoc.get("project", {}))  # type:ignore
            name: str | None = toml_project.get("name", None)
            if name is not None:  # pragma: no cover
                package_names.append(name)
        return package_names
