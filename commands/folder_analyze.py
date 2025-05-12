import os

def run(args):
    path = args.path
    if not os.path.isdir(path):
        print("Dossier introuvable")
        return

    print(f"Chemin absolu : {os.path.abspath(path)}")
    total_size = 0
    total_files = 0
    total_dirs = 0

    for root, dirs, files in os.walk(path):
        total_dirs += len(dirs)
        total_files += len(files)
        for f in files:
            try:
                fp = os.path.join(root, f)
                total_size += os.path.getsize(fp)
            except:
                pass

    print(f"Nombre de fichiers : {total_files}")
    print(f"Nombre de dossiers : {total_dirs}")
    print(f"Taille totale : {total_size} octets")
