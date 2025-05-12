---

### **`COMMANDS.md`**

```markdown
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
* `--inventory` : Lists the files in the folder, showing their extensions and file types.
* `--recursive` : Analyzes files in subdirectories as well.
* `--timestamp` : Includes file timestamps (modified, accessed, created).
* `--size` : Displays the size breakdown of each file in the folder.

### Example:

```bash
filder-info folder /home/user/Documents --human --recursive --size
```

## 2. `file` - File Analysis

The `file` command is used to analyze a single file. It provides metadata, timestamps, and other file-related information.

### Syntax:

```bash
filder-info file /path/to/file [options]
```

### Options:

* `--extra` : Displays additional file information such as permissions, owner, and group.
* `--timestamps` : Displays the file's creation, modification, and access times.
* `--size` : Displays the size of the file.

### Example:

```bash
filder-info file /path/to/file --extra --timestamps
```

## Output Formats:

* **Human-readable**: This is the default format for displaying information, optimized for clarity and readability.
* **JSON**: A machine-readable output format, useful for further processing or integration with other tools.

```

---

### 📝 Récapitulatif :
- **`README.md`** : Introduction au projet, installation et guide d'utilisation de base.
- **`USAGE.md`** : Détails sur l'utilisation des commandes et options avec exemples.
- **`COMMANDS.md`** : Liste complète des commandes disponibles, avec toutes les options détaillées.
