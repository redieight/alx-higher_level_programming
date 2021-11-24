#!/usr/bin/python3
def update_dictionary(my_dict, key, value):

    if key in my_dict:
        del my_dict[key]
        my_dict.update({key: value})
    else:
        my_dict.update({key: value})

    return my_dict
