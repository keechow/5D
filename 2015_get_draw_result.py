from parsing_module import print_each
from parsing_module3 import get_data
from port2excel import port_num
from combine_module import str_combine
from combine_module import combine
from sorting_module import sort
        # sort(combined_result, prize_cat)
        # 0 = number,    1 = Total,      2 = Top3
        # 3 = 1st Prize, 4 = 2nd Prize,  5 = 3rd Prize
        # 6 = Starter,   7 = Consolation
from num_cat_sort_module import num_cat_sorter
        # num_cat_sorter(combined_result, desired num_cat)
        # 1 = i24    2 = i12    3 = i4    4 = i1    0 = i6
        # only num from desired_num cat are returned
from num_cat_sort_module import result_separator
        # return a list with all result separated according to num_cat
        # [0] = i24     [1] = i12       [2] = i6
        # [3] = i4      [4] = i1  

from date_simulator import date_creator

from file_handler import write_to
        # str_combine() has to be used to produce string data suitable for saving into txt file
YEAR = 2012

jan = date_creator(YEAR, 1)
feb = date_creator(YEAR, 2)
mar = date_creator(YEAR, 3)
apr = date_creator(YEAR, 4)
may = date_creator(YEAR, 5)
jun = date_creator(YEAR, 6)
jul = date_creator(YEAR, 7)
aug = date_creator(YEAR, 8)
sep = date_creator(YEAR, 9)
octo = date_creator(YEAR, 10)
nov = date_creator(YEAR, 11)
dec = date_creator(YEAR, 12)

wed = [jan[0],feb[0],mar[0],apr[0],may[0],jun[0],jul[0],aug[0],sep[0],octo[0],nov[0],dec[0]]
sat = [jan[1],feb[1],mar[1],apr[1],may[1],jun[1],jul[1],aug[1],sep[1],octo[1],nov[1],dec[1]]
sun = [jan[2],feb[2],mar[2],apr[2],may[2],jun[2],jul[2],aug[2],sep[2],octo[2],nov[2],dec[2]]

wed_result = []
wed_day_result = []
sat_result = []
sat_day_result = []
sun_result = []
sun_day_result = []
for month in sat:
    for day in month:
        print "Getting result for: " + str(day)
        try:
            raw_result = get_data(day)
        except:
            print "ERROR while parsing: " + str(day)
            continue
        sat_combined_result = str_combine(raw_result)
        for each in sat_combined_result:
            sat_day_result.append(sat_combined_result)
print "sat_day_result completed\n"
for month in wed:
    for day in month:
        print "Getting result for: " + str(day)
        try:
            raw_result = get_data(day)
        except:
            print "ERROR while parsing: " + str(day)
            continue
        wed_combined_result = str_combine(raw_result)
        for each in wed_combined_result:
            wed_day_result.append(wed_combined_result)
print "wed_day_result completed\n"
for month in sun:
    for day in month:
        print "Getting result for: " + str(day)
        try:
            raw_result = get_data(day)
        except:
            print "ERROR while parsing: " + str(day)
            continue
        sun_combined_result = str_combine(raw_result)
        for each in sun_combined_result:
            sun_day_result.append(sun_combined_result)
print "sun_day_result completed\n"

## wed_day_result, sat_day_result, sun_day_result are lists containing list element with each day draw result
## list within list cannot work with write_to module
## we need to break list with list element into a long list with str element to work with write_to
for each_month in wed_day_result:
    for each_day in each_month:
        wed_result.append(each_day)
for each_month in sat_day_result:
    for each_day in each_month:
        sat_result.append(each_day)
for each_month in sun_day_result:
    for each_day in each_month:
        sun_result.append(each_day)



print "Save all result"
print "Wednesday"
write_to(wed_result)
print "Saturday"
write_to(sat_result)
print "Sunday"
write_to(sun_result)
print "Saving all combined result completed"
##print
##print
##print "Save i12 num with TOP3 sort"
##print "wednesday"
##write_to(sort(num_cat_sorter(wed_result,2),2))
##print "sat"
##write_to(sort(num_cat_sorter(sat_result,2),2))
##print "sun"
##write_to(sort(num_cat_sorter(sun_result,2),2))

print "========== END OF EXECUTION =========="



#Below are Testing codes
"""

raw_result = get_data()
        # Get result list based on date range entered

combined_result = combine(raw_result)
        # Combine number and occurrences into same element

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
"""
