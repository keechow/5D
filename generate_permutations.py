"""
Name: generate_permutations.py
Objective: Generate a list of permutation numbers given a number
Params: 4 digit num type<str>
Output: List of 4 digit number type<str>
Author: The Echo Telion Project <echo.telion@gmail.com>

"""

import itertools

def gen_perm(num):
    #num given is type<str>
    # we need to convert each digit to type<int> and append into a list
    # this is fit in itertools.permtutations format
    lst_num = []
    for each_digit in num:
        int_num = int(each_digit)
        lst_num.append(int_num)

    sorted_lst_num = sorted(lst_num)

    lst_perm = list(itertools.permutations(lst_num))
    str_lst_num = []
    for each in lst_perm:
        digit = ""
        for each_d in each:
            digit += str(each_d)
        if not digit in str_lst_num:
            str_lst_num.append(digit)

    return str_lst_num

## ========== Below are codes for testing ========== ##
"""
num_list = ["1234","1124","1112","1111"]

for each in num_list:
    print len(gen_perm(each))

"""
