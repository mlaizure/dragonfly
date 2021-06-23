def terminal_chart(data):
    """prints key, value pairs to stdout in pretty format"""
    current_max = 0

    # finds longest file name length to determine spacing for printing
    for key in data:
        l = len(key)
        if l > current_max:
            current_max = l

    # prints dict to stdout
    for key in sorted(data, key=data.get, reverse=True):
        print("{}{} | {}".format(key, (current_max - len(key)) * ' ',
                                 data[key]))
