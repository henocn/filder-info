import argparse
from commands import file_analyze, folder_analyze

def main():
    parser = argparse.ArgumentParser(prog="filder-info", description="Analyse de fichiers et de dossiers")
    subparsers = parser.add_subparsers(dest="command")

    file_parser = subparsers.add_parser("file", help="Analyser un fichier")
    file_parser.add_argument("path", help="Chemin du fichier")
    file_parser.set_defaults(func=file_analyze.run)

    folder_parser = subparsers.add_parser("folder", help="Analyser un dossier")
    folder_parser.add_argument("path", help="Chemin du dossier")
    folder_parser.set_defaults(func=folder_analyze.run)

    args = parser.parse_args()
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
