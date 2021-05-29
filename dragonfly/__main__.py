"""Main file for dragonfly function"""
import sys


opts = [opt for opt in sys.argv[1:] if opt.startswith("--")]


def main():
    """Main func"""
    if "--version" in opts:
        print("0.1.0")
    if "--noises" in opts:
        print("bzzz bzzz bzzz")
    if "--help" in opts:
        print(
            "\nPlease type 'dragonfly' followed by "
            "the name of the file or folder you wish "
            "to receive commit data from\n"
            "\t--version\tprint version\n"
            "\t--help\t   print this message\n")

if __name__ == "__main__":
    main()
