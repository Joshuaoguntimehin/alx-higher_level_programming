def replace_in_list(my_list, idx, element):
    if idx <0:
        return idx
    if idx >len(my_list):
        return my_list
     my_list[idx] = element
    return my_list

