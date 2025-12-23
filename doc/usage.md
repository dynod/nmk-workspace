# Usage

To use this plugin in your **`nmk`** project, insert this reference in your **nmk.yml** main file:
```yaml
refs:
    - pip://nmk-workspace!plugin.yml
```

Just after a workspace clone (or at any time you may want to update all your projects from remote repositories), the **{ref}`workspace.sync<workspace.sync>`** task can be used; it will:
* recursively update all submodules at their latest revision
* checkout the corresponding branch locally

Then, when using any of the following metatasks, this task will be triggered as well on all subprojects (submodules) of this project:
* **clean** -- see **{ref}`workspace.clean<workspace.clean>`**
* **setup** -- see **{ref}`workspace.setup<workspace.setup>`**
* **build** -- see **{ref}`workspace.build<workspace.build>`**
* **tests** -- see **{ref}`workspace.tests<workspace.tests>`**
* **package** -- see **{ref}`workspace.package<workspace.package>`**

```{note}
By default, subprojects builds are triggered only in CI (i.e. not with local builds). This behavior can be overridden by setting **{ref}`${workspaceDisableLocalTasks}<workspaceDisableLocalTasks>`** config item to **false**.
```
