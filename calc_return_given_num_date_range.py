"""
Name: calc_return_given_num_date_range.py
Objective: get total winning for a set of specified num
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

from num_analysis import check_num_cat
        #determine the category for num

import prize_calc

from generate_permutations import gen_perm


def getKey(item):     # for sorting list [['1234',50],['4567',99],[6789],22]
    return item[1]

def analyze_num_bought(num_bought, start_date, end_date):

        
    ## ========== WEB PARSING STAGE ========== ##
<<<<<<< HEAD
    print 'raw_result = get_data("2015/09/01","2015/09/30")'

    raw_result = get_data("2015/09/01","2015/09/30")
=======
    print "Getting winnings data: " + start_date + " - " + end_date

    raw_result = get_data(start_date, end_date)
>>>>>>> winnings

    combined_result = combine(raw_result)

    i24 = num_cat_sort_module.get_i24(combined_result)
    i12 = num_cat_sort_module.get_i12(combined_result)
    i6 = num_cat_sort_module.get_i6(combined_result)
    i4 = num_cat_sort_module.get_i4(combined_result)



    ## ========== CALCULATE THE NUM OF DRAW WITHIN STIPULATED RANGE ==========#

    draw_count = 0
    for each_draw in combined_result:
        draw_count += each_draw[3]

    ## ========== GET WINNING FOR EACH NUM ========== ##

    i24_num_winning = {}
    for each_draw in i24:
        num = each_draw[0]
        amount = prize_calc.i24_prize_calc(each_draw)

        if num in i24_num_winning:
            i24_num_winning[num] += amount
        else:
            i24_num_winning[num] = amount

    i12_num_winning = {}
    for each_draw in i12:
        num = each_draw[0]
        amount = prize_calc.i12_prize_calc(each_draw)

        if num in i12_num_winning:
            i12_num_winning[num] += amount
        else:
            i12_num_winning[num] = amount
    
    i6_num_winning = {}
    for each_draw in i6:
        num = each_draw[0]
        amount = prize_calc.i6_prize_calc(each_draw)

        if num in i6_num_winning:
            i6_num_winning[num] += amount
        else:
            i6_num_winning[num] = amount

    i4_num_winning = {}
    for each_draw in i4:
        num = each_draw[0]
        amount = prize_calc.i4_prize_calc(each_draw)

        if num in i4_num_winning:
            i4_num_winning[num] += amount
        else:
            i4_num_winning[num] = amount

    ## ========== CHECK NUM-WINNING DICT AGAINST GIVEN NUM LIST ========== ##

    num_hit = []    #list of num that hit
    total_winning = 0        # store total winning
    all_num_cat_winning = {24:i24_num_winning,12:i12_num_winning,6:i6_num_winning,4:i4_num_winning}
            #dict mapping each num_cat to its winning
    
    for each_num in num_bought:
        each_num_perm = gen_perm(each_num)    # generate all possible permutations for num bought
        num_cat = check_num_cat(each_num)    
        num_winning = all_num_cat_winning[num_cat]
        for each_perm in each_num_perm:
            str_each_num = str(each_perm)
            if str_each_num in num_winning:
                total_winning += num_winning[str_each_num]
                new = [str_each_num, num_winning[str_each_num]]
                num_hit.append(new)

    sorted_num_hit = sorted(num_hit, key=getKey, reverse=True)

    return_lst = [total_winning, draw_count, sorted_num_hit]

    return return_lst

def get_winning_data(begin_date, end_date):
    ## ========== GET DATA FROM WEBSITE ========== ##
    date_begin = begin_date
    date_end = end_date
    print "Parsing data from " + date_begin + " to " + date_end
    raw_data = get_data(date_begin, date_end)


    ## ========== CONVERT RAW DATA INTO USABLE FORM  ==========##
    combined_data = combine(raw_data)
            #combine separated data for one number into one element

    i24 = num_cat_sort_module.get_i24(combined_data)
    i12 = num_cat_sort_module.get_i12(combined_data)
    i6 = num_cat_sort_module.get_i6(combined_data)
    i4 = num_cat_sort_module.get_i4(combined_data)
            #separate combined_data into respective num_cat

    i24_num = []
    for each in i24:
        i24_num.append(each[0])
    i12_num = []
    for each in i12:
        i12_num.append(each[0])
    i6_num = []
    for each in i6:
        i6_num.append(each[0])
    i4_num = []
    for each in i4:
        i4_num.append(each[0])
            # we extract 4D number from each num_cat
    
    i24_winnings = analyze_num_bought(i24_num[30:40])
    i12_winnings = analyze_num_bought(i12_num[:10])
    i6_winnings = analyze_num_bought(i6_num[:10])
    i4_winnings = analyze_num_bought(i4_num[:10])
            #put each num_cat into calculator to get
            #[total_winning, draw_count, sorted_num_hit]

    return [i24_winnings,i12_winnings,i6_winnings,i4_winnings]

def get_i24win_data(begin_date, end_date, result_date_start, result_date_end):
    # take in begin_date & end_date for past result data collection
    # take in result_date_start & result_date_end to pass it to analyze_num_bought function
    ## ========== GET DATA FROM WEBSITE ========== ##
    date_begin = begin_date
    date_end = end_date
    
    print "Parsing data from " + date_begin + " to " + date_end
    raw_data = get_data(date_begin, date_end)


    ## ========== CONVERT RAW DATA INTO USABLE FORM  ==========##
    combined_data = combine(raw_data)
            #combine separated data for one number into one element

    i_num = num_cat_sort_module.get_i24(combined_data)

    num = []
    for each in i_num:
        num.append(each[0])
    
    _10 = analyze_num_bought(num[:10], result_date_start, result_date_end)
    _20 = analyze_num_bought(num[10:20], result_date_start, result_date_end)
    _30 = analyze_num_bought(num[20:30], result_date_start, result_date_end)
    _40 = analyze_num_bought(num[30:40], result_date_start, result_date_end)
    _50 = analyze_num_bought(num[40:50], result_date_start, result_date_end)
    _60 = analyze_num_bought(num[50:60], result_date_start, result_date_end)
    _70 = analyze_num_bought(num[60:70], result_date_start, result_date_end)

    print "[:10]"
    print _10
    print
    print "[10:20]"
    print _20
    print
    print "[20:30]"
    print _30
    print
    print "[30:40]"
    print _40
    print
    print "[40:50]"
    print _50
    print
    print "[50:60]"
    print _60
    print
    print "[60:70]"
    print _70
    print

def get_i12win_data(begin_date, end_date, result_date_start, result_date_end):
    # take in begin_date & end_date for past result data collection
    # take in result_date_start & result_date_end to pass it to analyze_num_bought function
    ## ========== GET DATA FROM WEBSITE ========== ##
    date_begin = begin_date
    date_end = end_date
    
    print "Parsing data from " + date_begin + " to " + date_end
    raw_data = get_data(date_begin, date_end)


    ## ========== CONVERT RAW DATA INTO USABLE FORM  ==========##
    combined_data = combine(raw_data)
            #combine separated data for one number into one element

    i_num = num_cat_sort_module.get_i12(combined_data)

    num = []
    for each in i_num:
        num.append(each[0])
    
    _10 = analyze_num_bought(num[:10], result_date_start, result_date_end)
    _20 = analyze_num_bought(num[10:20], result_date_start, result_date_end)
    _30 = analyze_num_bought(num[20:30], result_date_start, result_date_end)
    _40 = analyze_num_bought(num[30:40], result_date_start, result_date_end)
    _50 = analyze_num_bought(num[40:50], result_date_start, result_date_end)
    _60 = analyze_num_bought(num[50:60], result_date_start, result_date_end)
    _70 = analyze_num_bought(num[60:70], result_date_start, result_date_end)

    print "[:10]"
    print _10
    print
    print "[10:20]"
    print _20
    print
    print "[20:30]"
    print _30
    print
    print "[30:40]"
    print _40
    print
    print "[40:50]"
    print _50
    print
    print "[50:60]"
    print _60
    print
    print "[60:70]"
    print _70
    print 
                        
def get_i6win_data(begin_date, end_date, result_date_start, result_date_end):
    # take in begin_date & end_date for past result data collection
    # take in result_date_start & result_date_end to pass it to analyze_num_bought function
    ## ========== GET DATA FROM WEBSITE ========== ##
    date_begin = begin_date
    date_end = end_date
    
    print "Parsing data from " + date_begin + " to " + date_end
    raw_data = get_data(date_begin, date_end)


    ## ========== CONVERT RAW DATA INTO USABLE FORM  ==========##
    combined_data = combine(raw_data)
            #combine separated data for one number into one element

    i_num = num_cat_sort_module.get_i6(combined_data)

    num = []
    for each in i_num:
        num.append(each[0])
    
    _10 = analyze_num_bought(num[:10], result_date_start, result_date_end)
    _20 = analyze_num_bought(num[10:20], result_date_start, result_date_end)
    _30 = analyze_num_bought(num[20:30], result_date_start, result_date_end)
    _40 = analyze_num_bought(num[30:40], result_date_start, result_date_end)
    _50 = analyze_num_bought(num[40:50], result_date_start, result_date_end)
    _60 = analyze_num_bought(num[50:60], result_date_start, result_date_end)
    _70 = analyze_num_bought(num[60:70], result_date_start, result_date_end)

    print "[:10]"
    print _10
    print
    print "[10:20]"
    print _20
    print
    print "[20:30]"
    print _30
    print
    print "[30:40]"
    print _40
    print
    print "[40:50]"
    print _50
    print
    print "[50:60]"
    print _60
    print
    print "[60:70]"
    print _70
    print
    
def get_i4win_data(begin_date, end_date, result_date_start, result_date_end):
    # take in begin_date & end_date for past result data collection
    # take in result_date_start & result_date_end to pass it to analyze_num_bought function
    ## ========== GET DATA FROM WEBSITE ========== ##
    date_begin = begin_date
    date_end = end_date
    
    print "Parsing data from " + date_begin + " to " + date_end
    raw_data = get_data(date_begin, date_end)


    ## ========== CONVERT RAW DATA INTO USABLE FORM  ==========##
    combined_data = combine(raw_data)
            #combine separated data for one number into one element

    i_num = num_cat_sort_module.get_i4(combined_data)

    num = []
    for each in i_num:
        num.append(each[0])
    
    _10 = analyze_num_bought(num[:10], result_date_start, result_date_end)
    _20 = analyze_num_bought(num[10:20], result_date_start, result_date_end)
    _30 = analyze_num_bought(num[20:30], result_date_start, result_date_end)
    _40 = analyze_num_bought(num[30:40], result_date_start, result_date_end)
    _50 = analyze_num_bought(num[40:50], result_date_start, result_date_end)
    _60 = analyze_num_bought(num[50:60], result_date_start, result_date_end)
    _70 = analyze_num_bought(num[60:70], result_date_start, result_date_end)

    print "[:10]"
    print _10
    print
    print "[10:20]"
    print _20
    print
    print "[20:30]"
    print _30
    print
    print "[30:40]"
    print _40
    print
    print "[40:50]"
    print _50
    print
    print "[50:60]"
    print _60
    print
    print "[60:70]"
    print _70
    print
    
## ========== BELOW ARE TESTING CODES ========== ##
