# Tasks

The **`nmk-workspace`** plugin defines the tasks described below.

## Setup tasks

All tasks in this chapter are dependencies of the base [**`setup`**](https://nmk-base.readthedocs.io/en/stable/tasks.html#setup-task) task.

(workspace.setup)=
### **`workspace.setup`** -- subprojects setup

This task iterates on specified subprojects, and call their own [**`setup`**](https://nmk-base.readthedocs.io/en/stable/tasks.html#setup-task) task.

| Property | Value/description |
|-         |-
| builder           | {py:class}`nmk_workspace.builders.SubProjectsBuilder`
| if                | {ref}`${workspaceBuildEnabled.setup}<workspaceBuildEnabled>`
| root              | [**`${PROJECTDIR}`**](https://nmk.readthedocs.io/en/stable/file.html#built-in-config-items)
| to_build_first    | {ref}`${workspaceSubProjectsToBuildFirst}<workspaceSubProjectsToBuildFirst>`
| to_build          | {ref}`${workspaceSubProjectsToBuild}<workspaceSubProjectsToBuild>`
| to_build_after    | {ref}`${workspaceSubProjectsToBuildAfter}<workspaceSubProjectsToBuildAfter>`
| excluded          | {ref}`${workspaceSubProjectsToExclude}<workspaceSubProjectsToExclude>`
| args              | setup {ref}`${workspaceBuildExtraArgs}<workspaceBuildExtraArgs>`
| ignore_failures   | {ref}`${workspaceBuildIgnoreFailures.setup}<workspaceBuildIgnoreFailures>`


## Build tasks

All tasks in this chapter are dependencies of the base [**`build`**](https://nmk-base.readthedocs.io/en/stable/tasks.html#build-task) task.

(workspace.build)=
### **`workspace.build`** -- subprojects build

This task iterates on specified subprojects, and call their own [**`build`**](https://nmk-base.readthedocs.io/en/stable/tasks.html#build-task) task.

| Property | Value/description |
|-         |-
| builder           | {py:class}`nmk_workspace.builders.SubProjectsBuilder`
| if                | {ref}`${workspaceBuildEnabled.build}<workspaceBuildEnabled>`
| root              | [**`${PROJECTDIR}`**](https://nmk.readthedocs.io/en/stable/file.html#built-in-config-items)
| to_build_first    | {ref}`${workspaceSubProjectsToBuildFirst}<workspaceSubProjectsToBuildFirst>`
| to_build          | {ref}`${workspaceSubProjectsToBuild}<workspaceSubProjectsToBuild>`
| to_build_after    | {ref}`${workspaceSubProjectsToBuildAfter}<workspaceSubProjectsToBuildAfter>`
| excluded          | {ref}`${workspaceSubProjectsToExclude}<workspaceSubProjectsToExclude>`
| args              | build {ref}`${workspaceBuildExtraArgs}<workspaceBuildExtraArgs>`
| ignore_failures   | {ref}`${workspaceBuildIgnoreFailures.build}<workspaceBuildIgnoreFailures>`


## Tests tasks

All tasks in this chapter are dependencies of the base [**`tests`**](https://nmk-base.readthedocs.io/en/stable/tasks.html#tests-task) task.

(workspace.tests)=
### **`workspace.tests`** -- subprojects tests

This task iterates on specified subprojects, and call their own [**`tests`**](https://nmk-base.readthedocs.io/en/stable/tasks.html#tests-task) task.

| Property | Value/description |
|-         |-
| builder           | {py:class}`nmk_workspace.builders.SubProjectsBuilder`
| if                | {ref}`${workspaceBuildEnabled.tests}<workspaceBuildEnabled>`
| root              | [**`${PROJECTDIR}`**](https://nmk.readthedocs.io/en/stable/file.html#built-in-config-items)
| to_build_first    | {ref}`${workspaceSubProjectsToBuildFirst}<workspaceSubProjectsToBuildFirst>`
| to_build          | {ref}`${workspaceSubProjectsToBuild}<workspaceSubProjectsToBuild>`
| to_build_after    | {ref}`${workspaceSubProjectsToBuildAfter}<workspaceSubProjectsToBuildAfter>`
| excluded          | {ref}`${workspaceSubProjectsToExclude}<workspaceSubProjectsToExclude>`
| args              | tests {ref}`${workspaceBuildExtraArgs}<workspaceBuildExtraArgs>`
| ignore_failures   | {ref}`${workspaceBuildIgnoreFailures.tests}<workspaceBuildIgnoreFailures>`


## Package tasks

All tasks in this chapter are dependencies of the base [**`package`**](https://nmk-base.readthedocs.io/en/stable/tasks.html#package-task) task.

(workspace.package)=
### **`workspace.package`** -- subprojects package

This task iterates on specified subprojects, and call their own [**`package`**](https://nmk-base.readthedocs.io/en/stable/tasks.html#package-task) task.

| Property | Value/description |
|-         |-
| builder           | {py:class}`nmk_workspace.builders.SubProjectsBuilder`
| if                | {ref}`${workspaceBuildEnabled.package}<workspaceBuildEnabled>`
| root              | [**`${PROJECTDIR}`**](https://nmk.readthedocs.io/en/stable/file.html#built-in-config-items)
| to_build_first    | {ref}`${workspaceSubProjectsToBuildFirst}<workspaceSubProjectsToBuildFirst>`
| to_build          | {ref}`${workspaceSubProjectsToBuild}<workspaceSubProjectsToBuild>`
| to_build_after    | {ref}`${workspaceSubProjectsToBuildAfter}<workspaceSubProjectsToBuildAfter>`
| excluded          | {ref}`${workspaceSubProjectsToExclude}<workspaceSubProjectsToExclude>`
| args              | package {ref}`${workspaceBuildExtraArgs}<workspaceBuildExtraArgs>`
| ignore_failures   | {ref}`${workspaceBuildIgnoreFailures.package}<workspaceBuildIgnoreFailures>`


## Clean tasks

All tasks in this chapter are dependencies of the base [**`clean`**](https://nmk-base.readthedocs.io/en/stable/tasks.html#clean-task) task.

(workspace.clean)=
### **`workspace.clean`** -- subprojects clean

This task iterates on specified subprojects, and call their own [**`clean`**](https://nmk-base.readthedocs.io/en/stable/tasks.html#clean-task) task.

| Property | Value/description |
|-         |-
| builder           | {py:class}`nmk_workspace.builders.SubProjectsBuilder`
| if                | {ref}`${workspaceBuildEnabled.clean}<workspaceBuildEnabled>`
| root              | [**`${PROJECTDIR}`**](https://nmk.readthedocs.io/en/stable/file.html#built-in-config-items)
| to_build_first    | {ref}`${workspaceSubProjectsToBuildFirst}<workspaceSubProjectsToBuildFirst>`
| to_build          | {ref}`${workspaceSubProjectsToBuild}<workspaceSubProjectsToBuild>`
| to_build_after    | {ref}`${workspaceSubProjectsToBuildAfter}<workspaceSubProjectsToBuildAfter>`
| excluded          | {ref}`${workspaceSubProjectsToExclude}<workspaceSubProjectsToExclude>`
| args              | clean {ref}`${workspaceBuildExtraArgs}<workspaceBuildExtraArgs>`
| ignore_failures   | {ref}`${workspaceBuildIgnoreFailures.clean}<workspaceBuildIgnoreFailures>`
