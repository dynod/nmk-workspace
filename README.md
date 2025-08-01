# nmk-workspace
Workspace handling plugin for nmk build system

<!-- NMK-BADGES-BEGIN -->
[![License: MIT License](https://img.shields.io/github/license/dynod/nmk-workspace)](https://github.com/dynod/nmk-workspace/blob/main/LICENSE)
[![Checks](https://img.shields.io/github/actions/workflow/status/dynod/nmk-workspace/build.yml?branch=main&label=build%20%26%20u.t.)](https://github.com/dynod/nmk-workspace/actions?query=branch%3Amain)
[![Issues](https://img.shields.io/github/issues-search/dynod/nmk?label=issues&query=is%3Aopen+is%3Aissue+label%3Aplugin%3Aworkspace)](https://github.com/dynod/nmk/issues?q=is%3Aopen+is%3Aissue+label%3Aplugin%3Aworkspace)
[![Supported python versions](https://img.shields.io/badge/python-3.9%20--%203.13-blue)](https://www.python.org/)
[![PyPI](https://img.shields.io/pypi/v/nmk-workspace)](https://pypi.org/project/nmk-workspace/)
[![Code style: ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://astral.sh/ruff)
[![Code coverage](https://img.shields.io/codecov/c/github/dynod/nmk-workspace)](https://app.codecov.io/gh/dynod/nmk-workspace)
[![Documentation Status](https://readthedocs.org/projects/nmk-workspace/badge/?version=stable)](https://nmk-workspace.readthedocs.io/)
<!-- NMK-BADGES-END -->

This plugin helps to recursively trigger tasks in subprojects (i.e. usually projects located in git submodules), using a configurable build order.

## Usage

To use this plugin in your **`nmk`** project, insert this reference:
```yaml
refs:
    - pip://nmk-workspace!plugin.yml
```

## Documentation

This plugin documentation is available [here](https://nmk-workspace.readthedocs.io/)

## Issues

Issues for this plugin shall be reported on the [main  **`nmk`** project](https://github.com/dynod/nmk/issues), using the **plugin:workspace** label.
