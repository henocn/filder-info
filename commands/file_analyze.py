import os

def run(args):
    path = args.path
    if not os.path.isfile(path):
        print("Fichier introuvable")
        return

    print(f"Nom : {os.path.basename(path)}")
    print(f"Taille : {os.path.getsize(path)} octets")
    print(f"Chemin absolu : {os.path.abspath(path)}")
