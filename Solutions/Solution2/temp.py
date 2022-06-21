def parse_string(my_list):
    new_string = ''
    for i, j in enumerate(my_list):
        new_string += j
        if i < len(my_list) - 2:
            new_string += ', '
        elif i == len(my_list) - 2:
            new_string += ', and '