#!/usr/bin/python3
def replce_in_list(my_list, idx, element):
    if idx > len(my_list) - 1 or idx < 0:
        return my_list
    my_list[idx] = element
    return my_list
