"""This is the entry point of the program."""


def highest_number_cubed(limit):
    count = 1
    cube = 1
    a_list = []
    while cube < limit:
        cube = count * count * count
        a_list.append(count)
        count += 1        
    return a_list[len(a_list) - 2]
