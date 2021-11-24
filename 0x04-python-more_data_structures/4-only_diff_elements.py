#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    temp_list = list(set_1) + list(set_2)
    new_set = []

    for i in range(len(temp_list)):
        if temp_list.count(temp_list[i]) is 1:
            new_set.append(temp_list[i])

    return set(new_set)
