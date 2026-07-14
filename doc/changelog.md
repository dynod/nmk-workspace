# Changelog

Here are listed all the meaningfull changes done on **`nmk-workspace`** since version 1.0

```{note}
Only interface and important behavior changes are listed here.

The fully detailed changelog is also available on [Github](https://github.com/dynod/nmk-workspace/releases)
```

## Release 1.4.0

- New **{ref}`${workspaceSyncEnabled}<workspaceSyncEnabled>`** config item enabling the **{ref}`workspace.sync<workspace.sync>`** task.

## Release 1.3.0

- Updated documentation theme.
- New **{ref}`${workspacePythonSubProjects}<workspacePythonSubProjects>`** config item listing all python subprojects.
- Added {ref}`uv workspace members<uv-contrib>` generation in workspace-level **`pyproject.toml`** file.
- Add template support for buildenv 2.

## Release 1.2.0

- New **{ref}`${workspaceDisableLocalTasks}<workspaceDisableLocalTasks>`** config item, used to disable all subprojects builds locally (no effect in CI).
- New **{ref}`${workspaceSubModules}<workspaceSubModules>`** config item listing all project submodules.
- New **{ref}`workspace.sync<workspace.sync>`** task, used to synchronize all workspace submodules.

## Release 1.1.0

- New **{ref}`${workspaceBuildExtraArgsByStage}<workspaceBuildExtraArgsByStage>`** config item, used to specify nmk options per metatask.
- Build behavior changed for projects specified in **{ref}`${workspaceSubProjectsToBuildFirst}<workspaceSubProjectsToBuildFirst>`** and **{ref}`${workspaceSubProjectsToBuildAfter}<workspaceSubProjectsToBuildAfter>`** config items:<br>
  they are ignored in build if not also listed in **{ref}`${workspaceSubProjectsToBuild}<workspaceSubProjectsToBuild>`** config item.
