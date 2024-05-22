#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for y in range(x):
            if my_list[y]:
                print (f"{my_list[y]}", end="")
                count += 1
    except IndexError:
        pass
    finally:
        print()
        return count
