#!/usr.bin/python3
"""JSON functions"""


def to_json(adict, filename):
    """accept dict, convert to json string, save to file"""
    import json
    with open(filename + ".json", "w") as outfile:
        json.dump(adict, outfile)
