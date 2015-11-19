"""
Name: get_yearly_draw.py
Objective: Get single draw result for Wed, Sat, Sun for a year. Save it to separate txt file

Author: The Echo Telion Project <echo.telion@gmail.com>

"""
from parsing_module3 import get_data
from combine_module import str_combine
from num_cat_sort_module import num_cat_sorter
        # num_cat_sorter(combined_result, desired num_cat)
        # 1 = i24    2 = i12    3 = i4    4 = i1    0 = i6
        # only num from desired_num cat are returned
from sorting_module import sort
        # sort(combined_result, prize_cat)
        # 0 = number,    1 = Total,      2 = Top3
        # 3 = 1st Prize, 4 = 2nd Prize,  5 = 3rd Prize
        # 6 = Starter,   7 = Consolation
from date_simulator import date_creator
from file_handler import write_to
        # str_combine() has to be used to produce string data suitable for saving into txt file



### ===== generate dates for Wed, Sat, Sun. Used in url to parse draw result. ===== ###
YEAR = int(raw_input("Please enter year\n"))

wed = []
sat = []
sun = []
month_count = 1
while month_count < 13:
    wed.append(date_creator(YEAR,month_count)[0])
    sat.append(date_creator(YEAR,month_count)[1])
    sun.append(date_creator(YEAR,month_count)[2])
    month_count +=1
            ## jan_2014 = date_creator(2014, 1)
            ##    ...
            ## dec_2014 = date_creator(2014, 12)

            ## wed_2014 = [jan_2014[0],..., dec_2014[0]]
            ## sat_2014 = [jan_2014[1],..., dec_2014[1]]
            ## sun_2014 = [jan_2014[2],..., dec_2014[2]]


### ===== put dates generated to web parser to get data ===== ###
wed_result = []
wed_day_result = []
sat_result = []
sat_day_result = []
sun_result = []
sun_day_result = []

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
            wed_day_result.append(sat_combined_result)
print "wed_day_result completed\n"

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
            sun_day_result.append(sat_combined_result)
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


### ===== Save parsed data to separate txt file ===== ###
print "Save all result"
print "Wednesday"
write_to(wed_result)
print "Saturday"
write_to(sat_result)
print "Sunday"
write_to(sun_result)
print "Saving all combined result completed"
print
print
print "Save i12 num with TOP3 sort"
print "wednesday"
write_to(sort(num_cat_sorter(wed_result,2),2))
print "sat"
write_to(sort(num_cat_sorter(sat_result,2),2))
print "sun"
write_to(sort(num_cat_sorter(sun_result,2),2))

print "========== END OF EXECUTION =========="

