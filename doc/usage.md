# Usage

To use this plugin in your **`nmk`** project, insert this reference in your **nmk.yml** main file:
```yaml
refs:
    - pip://nmk-workspace!plugin.yml
```

Then, when using any of the following metatasks, this task will be triggered as well on all subprojects (submodules) of this project:
* clean
* setup
* build
* tests
* package
