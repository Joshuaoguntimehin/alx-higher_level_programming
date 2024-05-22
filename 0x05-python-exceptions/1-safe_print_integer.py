def safe_print_integer(value):
    try:
                if not isinstance(value, int):
                    return False
                print("{:d}".format(value))
    except IndexError:
        pass