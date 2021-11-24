#!/usr/bin/python3
def common_elements(set_1, set_2):
    temp_list = list(set_1) + list(set_2)
    new_set = []
    temp_list.sort()

    for i in range(len(temp_list)):
        if temp_list.count(temp_list[i]) > 1:
            new_set.append(temp_list[i])

    return set(new_set)
