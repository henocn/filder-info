filder-info

> A powerful command-line tool for analyzing files and folders with detailed reporting, custom filters, and advanced statistics.

It is particularly useful for developers, sysadmins, or anyone needing to extract structured information about filesystem elements.

## Features

- Analyze a single file: metadata, size, permissions, access timestamps, etc.
- Analyze an entire directory (recursive or not)
- Show file type proportions by extension
- Optional JSON output
- Human-readable formatting with colored CLI output (powered by [rich](https://github.com/Textualize/rich))

## Installation

```bash
pip install -i https://test.pypi.org/simple/ filder-info
```

## Usage

```bash
filder-info folder /path/to/folder --human --inventaire --ext
filder-info folder /path/to/folder --json --inventaire --ext
filder-info file /path/to/file --extra
```

## Requirements

- Python 3.7+
- rich

## Contributing

We welcome contributions! Feel free to fork the repository and submit pull requests.

Whether it's a bugfix, feature request, or performance improvement — your help is appreciated.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

[![TestPyPI](https://img.shields.io/pypi/v/filder-info?registry_uri=https://test.pypi.org/simple/)](https://test.pypi.org/project/filder-info/1.1.2/)