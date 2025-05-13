import os
import json
from datetime import datetime

from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text

console = Console()

def format_size(size, human=False):
    if not human:
        return f"{size} o"
    for unit in ['B','KB','MB','GB','TB']:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024
    return f"{size:.2f} PB"

def analyze_file(path, human=False, extra=False):
    if not os.path.isfile(path):
        raise FileNotFoundError(f"Fichier introuvable : {path}")

    stat = os.stat(path)
    info = {
        "path": os.path.abspath(path),
        "name": os.path.basename(path),
        "size": format_size(stat.st_size, human),
        "size_bytes": stat.st_size,
        "extension": os.path.splitext(path)[1] or "<no_ext>",
        "created": datetime.fromtimestamp(stat.st_ctime).isoformat(),
        "modified": datetime.fromtimestamp(stat.st_mtime).isoformat(),
        "accessed": datetime.fromtimestamp(stat.st_atime).isoformat()
    }

    if extra:
        info["is_symlink"] = os.path.islink(path)
        info["is_readable"] = os.access(path, os.R_OK)
        info["is_writable"] = os.access(path, os.W_OK)
        info["is_executable"] = os.access(path, os.X_OK)

    return info

def run(args):
    try:
        data = analyze_file(args.path, human=args.human, extra=args.extra)
    except FileNotFoundError as e:
        console.print(f"[bold red]{str(e)}[/bold red]")
        return

    if args.json:
        print(json.dumps(data, indent=2, ensure_ascii=False))
        return

    console.print(Panel.fit(f"[bold cyan]Analyse du fichier :[/bold cyan] {data['path']}", title="Fichier"))

    table = Table(show_lines=True)
    table.add_column("Clé", style="bold", justify="right")
    table.add_column("Valeur", style="green", overflow="fold")

    table.add_row("Nom", data["name"])
    table.add_row("Extension", data["extension"])
    table.add_row("Taille", data["size"])
    table.add_row("Taille (brute)", f"{data['size_bytes']} octets")
    table.add_row("Créé le", data["created"])
    table.add_row("Modifié le", data["modified"])
    table.add_row("Dernier accès", data["accessed"])

    if args.extra:
        table.add_row("Lien symbolique", str(data["is_symlink"]))
        table.add_row("Lisible", str(data["is_readable"]))
        table.add_row("Écriture", str(data["is_writable"]))
        table.add_row("Exécutable", str(data["is_executable"]))

    console.print(table)
