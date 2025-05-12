import os
import json
from datetime import datetime
from collections import defaultdict, Counter

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
        print("Dossier introuvable")
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

    print(f"Chemin absolu : {info['path']}")
    print(f"Taille totale : {info['total_size']}")
    print(f"Nombre de fichiers : {info['file_count']}")
    print(f"Nombre de dossiers : {info['folder_count']}")
    print(f"Créé le : {info['created']}")
    print(f"Dernière modification : {info['modified']}")

    if args.ext and "extensions" in info:
        print("\nRésumé par extension :")
        for ext, count in info["extensions"].items():
            print(f"  {ext} : {count} fichiers")

    if args.details:
        print("\nFichiers :")
        for f in info["files"]:
            print(f"  {f['path']} ({f['size']})")

    if args.inventaire and "inventaire" in info:
        inv = info["inventaire"]
        print("\nInventaire par extension :")
        for ext, meta in inv["par_extension"].items():
            print(f"  {ext} : {meta['nombre']} fichiers ({meta['proportion']}, {meta['taille']})")

        print("\nRépartition par taille :")
        for cls, val in inv["par_taille"].items():
            print(f"  {cls} : {val} fichiers")

        print(f"\nProfondeur maximale : {inv['profondeur_max']}")
