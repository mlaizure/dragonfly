def terminal_chart(data):
    """Prints key, value pairs to stdout in pretty format."""
    current_max = 0

    # Finds longest file name length to determine spacing for printing.
    for key in data:
        l = len(key)
        if l > current_max:
            current_max = l

    # Prints dictionary to stdout.
    for key in sorted(data, key=data.get, reverse=True):
        print("{}{} | {}".format(key, (current_max - len(key)) * ' ',
                                 data[key]))
