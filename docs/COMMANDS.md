# Available Commands for filder-info

This document describes all the commands available in the `filder-info` CLI tool.

## 1. `folder` - Folder Analysis

The `folder` command is used to analyze a folder and its contents, with detailed statistics on file types, sizes, and metadata.

### Syntax:
```bash
filder-info folder /path/to/folder [options]
````

### Options:

* `--human` : Displays the output in a human-readable format.
* `--json` : Outputs the analysis in JSON format.
* `--inventaire` : Lists the files in the folder, showing their extensions and file types.
* `--ext` : Statictics of extensions.

### Example:

```bash
filder-info folder /home/user/Documents --human --inventaire
```

## 2. `file` - File Analysis

The `file` command is used to analyze a single file. It provides metadata, timestamps, and other file-related information.

### Syntax:

```bash
filder-info file /path/to/file [options]
```

### Options:

* `--extra` : Displays additional file information such as permissions, owner, and group.
* `--human` : Displays the output in a human-readable format.
* `--json` : Outputs the analysis in JSON format.


### Example:

```bash
filder-info file /path/to/file --extra 
```
