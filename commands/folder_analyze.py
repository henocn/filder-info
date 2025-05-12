import os
import json
from datetime import datetime
from collections import defaultdict, Counter

from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text

console = Console()

def format_size(size, human=False):
    if not human:
        return f"{size} octets"
    for unit in ['B','KB','MB','GB','TB']:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024
    return f"{size:.2f} PB"

def classify_size(size):
    if size < 1024:
        return 'Petit (<1KB)'
    elif size < 1024 * 1024:
        return 'Moyen (<1MB)'
    elif size < 1024 * 1024 * 10:
        return 'Grand (<10MB)'
    else:
        return 'Très grand (≥10MB)'

def collect_folder_data(path, human=False, details=False, by_ext=False, inventaire=False):
    data = {
        "path": os.path.abspath(path),
        "total_size": 0,
        "file_count": 0,
        "folder_count": 0,
        "files": [],
        "extensions": {},
        "created": datetime.fromtimestamp(os.path.getctime(path)).isoformat(),
        "modified": datetime.fromtimestamp(os.path.getmtime(path)).isoformat()
    }

    ext_counter = Counter()
    size_classes = Counter()
    depth_levels = set()
    max_depth = 0
    size_by_ext = defaultdict(int)

    base_depth = len(os.path.abspath(path).split(os.sep))

    for root, dirs, files in os.walk(path):
        current_depth = len(os.path.abspath(root).split(os.sep)) - base_depth
        depth_levels.add(current_depth)
        max_depth = max(max_depth, current_depth)

        data["folder_count"] += len(dirs)
        data["file_count"] += len(files)

        for f in files:
            try:
                fp = os.path.join(root, f)
                size = os.path.getsize(fp)
                data["total_size"] += size

                ext = os.path.splitext(f)[1].lower() or "<no_ext>"

                if by_ext or inventaire:
                    ext_counter[ext] += 1
                    size_by_ext[ext] += size

                if inventaire:
                    size_classes[classify_size(size)] += 1

                if details:
                    data["files"].append({
                        "name": f,
                        "path": fp,
                        "size": format_size(size, human)
                    })

                if by_ext:
                    data["extensions"].setdefault(ext, 0)
                    data["extensions"][ext] += 1

            except:
                continue

    data["total_size"] = format_size(data["total_size"], human)
    if inventaire:
        total = sum(ext_counter.values())
        data["inventaire"] = {
            "par_extension": {
                ext: {
                    "nombre": count,
                    "proportion": f"{(count / total * 100):.2f}%",
                    "taille": format_size(size_by_ext[ext], human)
                }
                for ext, count in ext_counter.most_common()
            },
            "par_taille": dict(size_classes),
            "profondeur_max": max_depth
        }

    return data

def run(args):
    if not os.path.isdir(args.path):
        console.print(f"[bold red]Erreur : le dossier '{args.path}' est introuvable.[/bold red]")
        return

    info = collect_folder_data(
        args.path,
        human=args.human,
        details=args.details,
        by_ext=args.ext,
        inventaire=args.inventaire
    )

    if args.json:
        print(json.dumps(info, indent=2, ensure_ascii=False))
        return

    console.print(Panel.fit(f"[bold cyan]Analyse du dossier :[/bold cyan] {info['path']}", title="Dossier"))

    console.print(f"[bold yellow]Taille totale[/bold yellow] : {info['total_size']}")
    console.print(f"[bold green]Fichiers[/bold green] : {info['file_count']}")
    console.print(f"[bold blue]Dossiers[/bold blue] : {info['folder_count']}")
    console.print(f"Créé le : [magenta]{info['created']}[/magenta]")
    console.print(f"Modifié le : [magenta]{info['modified']}[/magenta]")

    if args.ext and "extensions" in info:
        table = Table(title="Fichiers par extension", show_lines=True)
        table.add_column("Extension", style="cyan", justify="center")
        table.add_column("Nombre", style="green", justify="right")
        for ext, count in info["extensions"].items():
            table.add_row(ext, str(count))
        console.print(table)

    if args.details:
        table = Table(title="Détail des fichiers", show_lines=True)
        table.add_column("Nom", style="white")
        table.add_column("Chemin", style="dim")
        table.add_column("Taille", justify="right", style="yellow")
        for f in info["files"]:
            table.add_row(f["name"], f["path"], f["size"])
        console.print(table)

    if args.inventaire and "inventaire" in info:
        inv = info["inventaire"]

        table = Table(title="Inventaire par extension", show_lines=True)
        table.add_column("Extension", style="cyan")
        table.add_column("Nombre", style="green", justify="right")
        table.add_column("Proportion", justify="right")
        table.add_column("Taille totale", justify="right", style="yellow")
        for ext, meta in inv["par_extension"].items():
            table.add_row(ext, str(meta["nombre"]), meta["proportion"], meta["taille"])
        console.print(table)

        table2 = Table(title="Répartition par taille", show_lines=True)
        table2.add_column("Classe", style="cyan")
        table2.add_column("Nombre de fichiers", style="green", justify="right")
        for cls, val in inv["par_taille"].items():
            table2.add_row(cls, str(val))
        console.print(table2)

        console.print(f"[bold cyan]🔎 Profondeur maximale du dossier :[/bold cyan] {inv['profondeur_max']}")
