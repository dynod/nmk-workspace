"""
Nmk workspace plugin config item resolvers.
"""

import re
from argparse import Namespace
from pathlib import Path

from nmk._internal.loader import NmkLoader
from nmk.logs import NmkLogger
from nmk.model.resolver import NmkListConfigResolver
from nmk.utils import run_with_logs

# Default nmk model definition file name
_DEFAULT_NMK_MODEL_FILE = "nmk.yml"

# Package name universal pattern (collect package names with letters, digits, underscores, dots, and dashes)
_PACKAGE_NAME_PATTERN = re.compile(r"^([a-zA-Z0-9_.-]+)")


class SubProjectsResolver(NmkListConfigResolver):
    """
    Resolver usable find sub-projects in the workspace tree.

    Default behavior is to look sub-projects by iterating through git submodules.
    (other behaviors may be implemented if needed later).
    """

    def get_value(self, name: str, root: str) -> list[str]:
        """
        Resolver for sub-projects list.

        :root: root path of the workspace
        :return: list of sub-projects paths relative to the workspace root
        """

        # Ask git for submodules paths
        root_path = Path(root)
        cp = run_with_logs(
            ["git", "submodule", "foreach", "--quiet", "--recursive", "echo $sm_path"], cwd=root_path
        )  # Note that $sm_path is a git variable, meaning this syntax is supported both on Linux and Windows
        nmk_models = []
        for candidate in cp.stdout.splitlines(keepends=False):
            # Only keep ones with a default nmk model file
            sub_project_path = candidate.strip()
            candidate_path = root_path / sub_project_path / _DEFAULT_NMK_MODEL_FILE
            if candidate_path.is_file():
                nmk_models.append(sub_project_path)
            else:
                NmkLogger.debug(f"Sub-project {sub_project_path} does not have a default nmk model file, skipping it.")
        return nmk_models


class FilteredProjectsResolver(NmkListConfigResolver):
    """
    Resolver usable to filter subprojects in the workspace tree, following provided conditions
    """

    def get_value(self, name: str, root: str, all_sub_projects: list[str], artifact_name_item: str, dependencies_item: str) -> list[str]:
        """
        Resolver for filtered projects list.

        :all_sub_projects: list of all sub-project paths (to be filtered)
        :root: root path of the workspace
        :artifact_name_item: property name used to identify the artifact name of the nmk project
        :dependencies_item: property name used to identify the dependencies of the nmk project
        :return: list of filtered project paths relative to the workspace root
        """

        # Parsed dependencies model
        projects_from_artifacts: dict[str, str] = {}
        artifacts_deps: dict[str, list[str]] = {}

        # Iterate through all sub-projects and filter them based on the provided conditions
        for sub_project in all_sub_projects:
            NmkLogger.debug(f">> Processing sub-project: {sub_project}")

            # Load sub-project model
            sub_project_path = Path(root) / sub_project / _DEFAULT_NMK_MODEL_FILE
            assert sub_project_path.is_file(), f"Sub-project {sub_project} does not have a default nmk model file"
            fake_args = Namespace(project=sub_project_path, root=None, no_cache=False, config=None, skipped_tasks=[])
            try:
                sub_project_model = NmkLoader(args=fake_args, with_logs=False).model
            except Exception as e:
                NmkLogger.error(f"Failed to load sub-project model for {sub_project}: {e}")
                raise e

            # Check for required item names in subproject model
            if (artifact_name_item not in sub_project_model.config) or (dependencies_item not in sub_project_model.config):
                NmkLogger.debug(f"Sub-project {sub_project} incompatible with this resolver, skipping it.")
                continue

            # Artifact name shouldn't be already known
            artifact_name = sub_project_model.config[artifact_name_item].value
            assert artifact_name not in projects_from_artifacts, (
                f"Artifact name {artifact_name} is already known (from sub-project {projects_from_artifacts[artifact_name]})"
            )
            projects_from_artifacts[artifact_name] = sub_project

            # Remember dependencies of the artifact (filtered by package name pattern)
            deps = [m.group(1) for m in map(_PACKAGE_NAME_PATTERN.search, sub_project_model.config[dependencies_item].value) if m]
            artifacts_deps[artifact_name] = deps

        # Rework dependencies to only include artifacts that are known
        artifacts_deps = {name: sorted(list(set(deps) & artifacts_deps.keys())) for name, deps in artifacts_deps.items()}

        ordered_artifacts = []

        # Recursive algorithm to traverse artifacts and their dependencies
        def _traverse_artifacts(artifact: str, refering_artifacts: list[str]):
            # Cyclic dependency?
            assert artifact not in refering_artifacts, f"Cyclic dependency: {artifact} referenced from artifacts {' -> '.join(refering_artifacts)}"

            # Traverse dependencies
            for dep in sorted(list(artifacts_deps[artifact] & artifacts_deps.keys())):
                _traverse_artifacts(dep, refering_artifacts + [artifact])

            # Add artifact if not already done
            if artifact not in ordered_artifacts:
                ordered_artifacts.append(artifact)

        # Second loop to sort sub-projects by dependencies
        for artifact in artifacts_deps:
            _traverse_artifacts(artifact, [])
        return [projects_from_artifacts[artifact] for artifact in ordered_artifacts]
