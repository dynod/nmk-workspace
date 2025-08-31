# Changelog

Here are listed all the meaningfull changes done on **`nmk-workspace`** since version 1.0

```{note}
Only interface and important behavior changes are listed here.

The fully detailed changelog is also available on [Github](https://github.com/dynod/nmk-workspace/releases)
```

## Release 1.1

### 1.1.0

* New **{ref}`${workspaceBuildExtraArgsByStage}<workspaceBuildExtraArgsByStage>`** config item, used to specify nmk options per metatask.
* Build behavior changed for projects specified in **{ref}`${workspaceSubProjectsToBuildFirst}<workspaceSubProjectsToBuildFirst>`** and **{ref}`${workspaceSubProjectsToBuildAfter}<workspaceSubProjectsToBuildAfter>`** config items:<br>
  they are ignored in build if not also listed in **{ref}`${workspaceSubProjectsToBuild}<workspaceSubProjectsToBuild>`** config item.