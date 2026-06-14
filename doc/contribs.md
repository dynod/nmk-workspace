# Contributions

The **`nmk-workspace`** plugin contributes to **`nmk`** features as described below.

## Plugin information

As other plugins, **`nmk-workspace`** registers its version and documentation link in [plugin information config items](https://nmk-base.readthedocs.io/en/stable/extend.html#plugin-information).

(uv-contrib)=

## Python workspace for uv

A workspace project may aim to be a [Python workspace for uv tool](https://docs.astral.sh/uv/concepts/projects/workspaces/). In this case it shall reference as well the **`nmk-python`** plugin in its **`nmk.yml`** file

**`nmk-workspace`** contributes to [${pythonprojectfileitems}](https://nmk-python.readthedocs.io/en/stable/config.html#pythonprojectfileitems) in order to add the Python sub-projects list to the [tool.uv.workspace](https://docs.astral.sh/uv/reference/settings/#workspace_members) item, from the **{ref}`${workspacePythonSubProjects}<workspacePythonSubProjects>`** computed list.
