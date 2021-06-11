#!/usr/bin/env python3
"""Main file for dragonfly function"""
from sys import argv
from dragonfly.analysis import analysis
from dragonfly.to_json_string import to_json
from dragonfly.heat_map1 import make_chart
from dragonfly.terminal import terminal_chart


opts = [opt for opt in argv[1:] if opt.startswith("--")]
args = [arg for arg in argv[1:] if arg not in opts]


def main():
    """Main func"""
    data = {}
    terminal_display = False
    gen_chart = False
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
            "\t--version   print version\n"
            "\t--help      print this message\n"
            "\t--terminal  print data in terminal\n"
            "\t--chart     generate pie chart of results\n")
        return
    if "--terminal" in opts:
        terminal_display = True
    if "--chart" in opts:
        gen_chart = True

    if len(args) == 1:
        data = analysis(args[0])
    elif len(args) == 2:
        data = analysis(args[0], args[1])
    else:
        print("usage: dragonfly ABSOLUTE_PATH_TO_REPO [BRANCH]\n"
              "\t--help   see more options\n")
        return

    if data is None:
        return

    if terminal_display:
        terminal_chart(data)
        return
    elif gen_chart:
        make_chart(data)
        print("heat_map1.png file generated")
        return
    else:
        to_json(data, 'drgnfly_analysis')
        print("drgnfly_analysis.json file generated")


if __name__ == "__main__":
    main()
