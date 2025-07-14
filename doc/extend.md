# Configuration Extension

As for all **`nmk`** projects config items, [**`nmk-workspace`** ones](config.md) are all overridable by other plug-ins and project files. But the ones described on this page are specifically designed to be extended.

## Build order

By default, this plugin will build all submodules nmk projects (in the submodules order), as listed by the {ref}`${workspaceSubProjects}<workspaceSubProjects>` item.

It is also possible to change this behavior by using the following config items:
* **{ref}`${workspaceSubProjectsToBuildFirst}<workspaceSubProjectsToBuildFirst>`**: List of subprojects to build before all the others.
  Example:
  ```yaml
  workspaceSubProjectsToBuildFirst:
      - path/to/some/tooling/project
      - path/to/some/api/project
  ```
* **{ref}`${workspaceSubProjectsToBuildAfter}<workspaceSubProjectsToBuildAfter>`**: List of subprojects to build after all the others.
  Example:
  ```yaml
  workspaceSubProjectsToBuildAfter:
      - path/to/some/top/level/project
  ```
* **{ref}`${workspaceSubProjectsToExclude}<workspaceSubProjectsToExclude>`**: List of patterns usable to exclude subproject from build.
  Example:
  ```yaml
  workspaceSubProjectsToExclude:
      - useless/*
  ```

## Build conditions

These config items can also be used to condition the subprojects build behavior:
* **{ref}`${workspaceBuildEnabled}<workspaceBuildEnabled>`**: Dict of enablement conditions for meta-tasks.
  Example:
  ```yaml
  workspaceBuildEnabled:
      package: false # Disable package build for subprojects
  ```
* **{ref}`${workspaceBuildIgnoreFailures}<workspaceBuildIgnoreFailures>`**: Dict of failures ignore options for meta-tasks.
  Example:
  ```yaml
  workspaceBuildIgnoreFailures:
      tests: false # Any failed test of any sub-project will make the full workspace test fail
  ```
