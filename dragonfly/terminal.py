def terminal_chart(data):
    current_max = 0
    for key in data:
        l = len(key)
        if l > current_max:
            current_max = l
    for key in sorted(data, key=data.get, reverse=True):
        print("{}{} | {}".format(key, (current_max - len(key)) * ' ',
                                 data[key]))
