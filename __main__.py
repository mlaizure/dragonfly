#!/usr/bin/env python3
"""Main file for dragonfly function"""
from sys import argv
from dragonfly.analysis import analysis
from dragonfly.to_json_string import to_json
from dragonfly.heat_map1 import make_chart


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
            "usage: dragonfly ABSOLUTE_PATH_TO_REPO [BRANCH]\n\n"
            "  Return commit data from given repository.\n\n"
            "Options:\n"
            "\t--version\tprint version\n"
            "\t--help\t   print this message\n")
        return

    if len(argv) == 2:
        data = analysis(argv[1])
    elif len(argv) == 3:
        data = analysis(argv[1], argv[2])
    else:
        print("usage: dragonfly ABSOLUTE_PATH_TO_REPO [BRANCH]\n"
              "\t--help\t see more options\n")
        return

    to_json(data, 'drgnfly_analysis')
    make_chart(data)


if __name__ == "__main__":
    main()
