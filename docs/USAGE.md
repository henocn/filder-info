# Usage Guide for filder-info

## Command Overview

`filder-info` provides two primary commands: **file** and **folder**. Each of these commands accepts various options that influence the type and format of the output.

## Command: `folder`

This command allows you to analyze an entire folder, recursively or not, showing various details about its contents.

### Basic Syntax:
```bash
filder-info folder /path/to/folder [options]
````

### Available Options:

* `--human` : Display output in a human-readable format (default).
* `--json` : Output the analysis results in JSON format.
* `--inventaire` : Show a list of files in the directory with their extensions and counts.
* `--details` : Show detailed information about each file, including size, type, and timestamps.

### Example:

```bash
filder-info folder /path/to/folder --human --recursive --inventory
```

## Command: `file`

This command analyzes a single file and displays various details about it, including its metadata, timestamps, and size.

### Basic Syntax:

```bash
filder-info file /path/to/file [options]
```

### Available Options:

* `--extra` : Show extra metadata, including permissions and ownership.
* `--human` : Human format with tab.
* `--json` : Output the analysis results in JSON format.

### Example:

```bash
filder-info file /path/to/file --human --extra
```