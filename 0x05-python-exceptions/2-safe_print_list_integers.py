#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    counter = 0
    try:
        for i in range(x):
            if isinstance(my_list[i], int) and i < x:
                print("{:d}".format(my_list[i]), end="")
                counter += 1
            else:
                continue
        print() 
    except IndexError:
        raise IndexError

    return counter
