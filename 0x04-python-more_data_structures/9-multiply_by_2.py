#!/usr/bin/python3
def multiply_by_2(my_dict):
    new = {}
    for key in my_dict:
        new.update({key: my_dict[key] * 2})

    return new
