import argparse
from commands import file_analyze, folder_analyze

def main():
    parser = argparse.ArgumentParser(prog="filder-info", description="Analyse de fichiers et de dossiers")
    subparsers = parser.add_subparsers(dest="command")

    file_parser = subparsers.add_parser("file", help="Analyser un fichier")
    file_parser.add_argument("path", help="Chemin vers le fichier")
    file_parser.add_argument("--human", action="store_true", help="Afficher les tailles lisibles")
    file_parser.add_argument("--extra", action="store_true", help="Afficher des métadonnées supplémentaires")
    file_parser.add_argument("--json", action="store_true", help="Sortie au format JSON")
    file_parser.set_defaults(func=file_analyze.run)

    folder_parser = subparsers.add_parser("folder", help="Analyser un dossier")
    folder_parser.add_argument("path", help="Chemin du dossier")
    folder_parser.add_argument("--details", action="store_true", help="Lister les fichiers avec leur taille")
    folder_parser.add_argument("--json", action="store_true", help="Afficher la sortie en JSON")
    folder_parser.add_argument("--human", action="store_true", help="Afficher les tailles dans un format lisible")
    folder_parser.add_argument("--ext", action="store_true", help="Afficher le résumé des extensions de fichiers")
    folder_parser.add_argument("--inventaire", action="store_true", help="Afficher l'inventaire détaillé du dossier")
    folder_parser.set_defaults(func=folder_analyze.run)

    args = parser.parse_args()
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
