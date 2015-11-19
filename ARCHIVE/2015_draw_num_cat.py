from parsing_module import print_each
from parsing_module2 import get_data
from combine_module import combine
from sorting_module import sort
        # sort(combined_result, prize_cat)
        # 0 = number,    1 = Total,      2 = Top3
        # 3 = 1st Prize, 4 = 2nd Prize,  5 = 3rd Prize
        # 6 = Starter,   7 = Consolation
from num_cat_sort_module import num_cat_sorter
        # num_cat_sorter(combined_result, desired num_cat)
        # 1 = i24    2 = i12    3 = i4    4 = i1    0 = i6
from num_cat_sort_module import result_separator
        # return a list with all result separated according to num_cat
        # [0] = i24     [1] = i12       [2] = i6
        # [3] = i4      [4] = i1  
count_i24 = []
count_i12 = []
count_i6 = []
count_i4 = []

        # we want to know i12 draw count for each draw

past_draw_date = [[3,4,6,7,10,11,14,17,18,21,24,25,27,28,31],[1,3,4,7,8,11,14,15,17,18,21,22,24,25,28],[1,3,4,7,8,11,14,15,18,21,22,25,28,29,31],[1,4,5,7,8,11,12,15,18,19,22,25,26,28,29],[2,3,5,6,9,10,13,16,17,20,23,24,26,27,30,31],[2,3,6,7,10,13,14,17,20,21,24,27,28],[1,4,5,8,11,12,15,18,19,22,25,26,29],[1,2,4,5,8,9,12,15,16,19,22,23,26,29,30],[1]]
month_counter = 1
while month_counter <= len(past_draw_date):
    for each_month in past_draw_date:
        for each_day in each_month:
            raw_result = get_data(month_counter, each_day)
            combined_result = combine(raw_result)
            separated_result = result_separator(combined_result)
            count_i24.append(len(separated_result[0]))
            count_i12.append(len(separated_result[1]))
            count_i6.append(len(separated_result[0]))
            count_i4.append(len(separated_result[3]))       #we just want to know the count
        month_counter += 1
print "i24 len: ", len(count_i24)
print "i12 len: ", len(count_i12)
print "i6 len: ", len(count_i6)
print "i4 len: ", len(count_i4)

print "==========End of execution=========="

#Below are Testing codes
"""
print "1 digit: ", len(list_result_num1)
print
print "2 digit: ", len(list_result_num2)
print
print "3 digit: ", len(list_result_num3)
print
print "4 digit: ", len(list_result_num4)
print
print "double digit: ", len(list_result_num_double)
print
print "Result len: ", len(combined_result)
print

#Pass draw dates
sep15 = [1]
aug15 = [1,2,4,5,8,9,12,15,16,19,22,23,26,29,30]
jul15 = [1,4,5,8,11,12,15,18,19,22,25,26,29]
jun15 = [2,3,6,7,10,13,14,17,20,21,24,27,28]
may15 = [2,3,5,6,9,10,13,16,17,20,23,24,26,27,30,31]
apr15 = [1,4,5,7,8,11,12,15,18,19,22,25,26,28,29]
mar15 = [1,3,4,7,8,11,14,15,18,21,22,25,28,29,31]
feb15 = [1,3,4,7,8,11,14,15,17,18,21,22,24,25,28]
jan15 = [3,4,6,7,10,11,14,17,18,21,24,25,27,28,31]

i12_draw_result = [10,10,6,8,9,9,10,9,9,9,7,10,7,12,6,11,9,10,6,11,5,11,8,9,13,13,9,11,7,11,12,11,7,8,9,8,16,10,9,9,10,9,8,11,12,9,13,13,13,11,10,10,7,7,6,7,8,14,13,11,7,7,8,7,12,9,12,11,12,11,8,7,7,9,13,8,7,12,13,11,11,5,10,15,15,8,9,7,10,7,8,11,11,12,9,8,11,9,9,9,14,9,9,13,10,4,12,9,12,11,13,14,9,6,11,16,10,12]

"""
