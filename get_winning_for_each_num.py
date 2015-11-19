"""
Name: get_winning_for_each_num.py
Objective: calculate total prize won by each num for the past 24 months
Author: The Echo Telion Project <echo.telion@gmail.com>

"""
from parsing_module4 import print_each
from parsing_module4 import get_data
from combine_module import str_combine
from combine_module import combine
import num_cat_sort_module
    #get_i24, get_i12, get_i6, get_i4, get_i1
    #get_all_result : [[i24],[i12],[i6],[i4],[i1]]
from sorting_module import sort
        # sort(combined_result, prize_cat)
        # 0 = number,    1 = Total,      2 = Top3
        # 3 = 1st Prize, 4 = 2nd Prize,  5 = 3rd Prize
        # 6 = Starter,   7 = Consolation

import prize_calc



## ===== WEB PARSING STAGE ===== ##

print "result_24m : 2013/09/01 to 2013/09/30\n"
result_24m_raw = get_data("2013/09/01", "2013/09/30")

print "result_23m : 2013/10/01 to 2013/10/31\n"
result_23m_raw = get_data("2013/10/01", "2013/10/31")

print "result_22m : 2013/11/01 to 2013/11/30\n"
result_22m_raw = get_data("2013/11/01", "2013/11/30")

print "result_21m : 2013/12/01 to 2013/12/31\n"
result_21m_raw = get_data("2013/12/01", "2013/12/31")

print "result_20m : 2014/01/01 to 2014/01/31\n"
result_20m_raw = get_data("2014/01/01", "2014/01/31")

print "result_19m : 2014/02/01 to 2014/02/28\n"
result_19m_raw = get_data("2014/02/01", "2014/02/28")

print "result_18m : 2014/03/01 to 2014/03/31\n"
result_18m_raw = get_data("2014/03/01", "2014/03/31")

print "result_17m : 2014/04/01 to 2014/04/30\n"
result_17m_raw = get_data("2014/04/01", "2014/04/30")

print "result_16m : 2014/05/01 to 2014/05/31\n"
result_16m_raw = get_data("2014/05/01", "2014/05/31")

print "result_15m : 2014/06/01 to 2014/06/30\n"
result_15m_raw = get_data("2014/06/01", "2014/06/30")

print "result_14m : 2014/07/01 to 2014/07/31\n"
result_14m_raw = get_data("2014/07/01", "2014/07/31")

print "result_13m : 2014/08/01 to 2014/08/31\n"
result_13m_raw = get_data("2014/08/01", "2014/08/31")

print "result_12m : 2014/09/01 to 2014/09/30\n"
result_12m_raw = get_data("2014/09/01", "2014/09/30")

print "result_11m : 2014/10/01 to 2014/10/31\n"
result_11m_raw = get_data("2014/10/01", "2014/10/31")

print "result_10m : 2014/11/01 to 2014/11/30\n"
result_10m_raw = get_data("2014/11/01", "2014/11/30")

print "result_9m : 2014/12/01 to 2014/12/31\n"
result_9m_raw = get_data("2014/12/01", "2014/12/31")

print "result_8m : 2015/01/01 to 2015/01/31\n"
result_8m_raw = get_data("2015/01/01", "2015/01/31")

print "result_7m : 2015/02/01 to 2015/02/28\n"
result_7m_raw = get_data("2015/02/01", "2015/02/28")

print "result_6m : 2015/03/01 to 2015/03/31\n"
result_6m_raw = get_data("2015/03/01", "2015/03/31")

print "result_5m : 2015/04/01 to 2015/04/30\n"
result_5m_raw = get_data("2015/04/01", "2015/04/30")

print "result_4m : 2015/05/01 to 2015/05/31\n"
result_4m_raw = get_data("2015/05/01", "2015/05/31")

print "result_3m : 2015/06/01 to 2015/06/30\n"
result_3m_raw = get_data("2015/06/01", "2015/06/30")

print "result_2m : 2015/07/01 to 2015/07/31\n"
result_2m_raw = get_data("2015/07/01", "2015/07/31")

print "result_1m : 2015/08/01 to 2015/08/31\n"
result_1m_raw = get_data("2015/08/01", "2015/08/31")

result_raw = [result_24m_raw,result_23m_raw,result_22m_raw,result_21m_raw,result_20m_raw,
              result_19m_raw,result_18m_raw,result_17m_raw,result_16m_raw,result_15m_raw,
              result_14m_raw,result_13m_raw,result_12m_raw,result_11m_raw,result_10m_raw,
              result_9m_raw,result_8m_raw,result_7m_raw,result_6m_raw,result_5m_raw,
              result_4m_raw,result_3m_raw,result_2m_raw,result_1m_raw]


## ===== Number Analysis ===== ##
result_combined = []
for each in result_raw:
    new = combine(each)
    result_combined.append(new)

     ## each num cat gets its own list
i24 = []
for each in result_combined:
    new =  num_cat_sort_module.get_i24(each)
    i24.append(new)
i12 = []
for each in result_combined:
    new = num_cat_sort_module.get_i12(each)
    i12.append(new)
i6 = []
for each in result_combined:
    new =  num_cat_sort_module.get_i6(each)
    i6.append(new)
i4 = []
for each in result_combined:
    new = num_cat_sort_module.get_i4(each)
    i4.append(new)

    ## calculate prize money won by each number ##
def getKey(item):
    # this is for sorting list
    return item[1]
    
i24_monthly_num_winning = []
i24_combined_num_winning = []
i24_combined_winning = {}

for each_month in i24:
    num_winning = {}
    lst_num_winning = []
    for each_draw in each_month:
        num = each_draw[0]
        amount = prize_calc.i24_prize_calc(each_draw)
        if num in num_winning:
            num_winning[num] += amount
        else:
            num_winning[num] = amount
        # put num and winning into dict to count winning amount
        if num in i24_combined_winning:
            i24_combined_winning[num] += amount
        else:
            i24_combined_winning[num] = amount
        # this part is for all month combined list
    for num, win in num_winning.items():
        new = [num, win]
        lst_num_winning.append(new)
        # convert dict back to list    
    i24_monthly_num_winning.append(sorted(lst_num_winning, key=getKey, reverse=True))
        # sort the list with highest wing first and append to whole i24 list
for num, win in i24_combined_winning.items():
    new = [num, win]
    i24_combined_num_winning.append(new)

i24_all24m_num_winning = sorted(i24_combined_num_winning, key=getKey, reverse=True)

i12_monthly_num_winning = []
i12_combined_num_winning = []
i12_combined_winning = {}

for each_month in i12:
    num_winning = {}
    lst_num_winning = []
    for each_draw in each_month:
        num = each_draw[0]
        amount = prize_calc.i12_prize_calc(each_draw)
        if num in num_winning:
            num_winning[num] += amount
        else:
            num_winning[num] = amount
        # put num and winning into dict to count winning amount
        if num in i12_combined_winning:
            i12_combined_winning[num] += amount
        else:
            i12_combined_winning[num] = amount
        # this part is for all month combined list
    for num, win in num_winning.items():
        new = [num, win]
        lst_num_winning.append(new)
        # convert dict back to list    
    i12_monthly_num_winning.append(sorted(lst_num_winning, key=getKey, reverse=True))
        # sort the list with highest wing first and append to whole i24 list
for num, win in i12_combined_winning.items():
    new = [num, win]
    i12_combined_num_winning.append(new)

i12_all24m_num_winning = sorted(i12_combined_num_winning, key=getKey, reverse=True)


i6_monthly_num_winning = []
for each_month in i6:
    num_winning = {}
    lst_num_winning = []
    for each_draw in each_month:
        num = each_draw[0]
        amount = prize_calc.i6_prize_calc(each_draw)
        if num in num_winning:
            num_winning[num] += amount
        else:
            num_winning[num] = amount
        # put num and winning into dict to count winning amount
    for num, win in num_winning.items():
        new = [num, win]
        lst_num_winning.append(new)
        # convert dict back to list
    i6_monthly_num_winning.append(sorted(lst_num_winning, key=getKey, reverse=True))


i4_monthly_num_winning = []
for each_month in i4:
    num_winning = {}
    lst_num_winning = []
    for each_draw in each_month:
        num = each_draw[0]
        amount = prize_calc.i4_prize_calc(each_draw)
        if num in num_winning:
            num_winning[num] += amount
        else:
            num_winning[num] = amount
        # put num and winning into dict to count winning amount
    for num, win in num_winning.items():
        new = [num, win]
        lst_num_winning.append(new)
        # convert dict back to list
    i4_monthly_num_winning.append(sorted(lst_num_winning, key=getKey, reverse=True))

## ========== PRINT RESULT ========== ##

print "========== END OF EXECUTION =========="
