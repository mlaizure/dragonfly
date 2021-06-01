"""Main file for dragonfly function"""
from sys import argv
from .analysis import analysis
from .to_json_string import to_json


opts = [opt for opt in argv[1:] if opt.startswith("--")]


def main():
    """Main func"""
    data = {}
    if "--version" in opts:
        print("0.1.0")
        return
    if "--noises" in opts:
        print("bzzz bzzz bzzz")
        return
    if "--help" in opts:
        print(
            "usage: dragonfly [folder/file]...\n\n"
            "  Return commit data from given folder or file.\n\n"
            "Options:\n"
            "\t--version\tprint version\n"
            "\t--help\t   print this message\n")
        return

    if len(argv) is 1:
        data = analysis(argv[1])
        to_json(data, drgnfly_analysis)
    if len(argv) is 2:
        data = analysis(argv[1], argv[2])
        to_json(data, drgnfly_analysis)

if __name__ == "__main__":
    main()
