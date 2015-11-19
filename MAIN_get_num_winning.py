"""
Name: MAIN_get_num_winning.py
Objective: get winnings for each num for the past 24 months
AUthor: The Echo Telion Project <echo.telion@gmail.com>

"""

from calc_return_given_num_date_range import get_winning_data
        #params: date range e.g. "2015/01/31","2015/03/31"
        #return a list with 4 elements
        # element 0: i24_winnings
        # element 1: i12_winnings
        # element 2: i6_winnings
        # element 3: i4_winnings

#24m : "2013/09/01","2015/08/31"
#12m : "2014/09/01","2015/08/31"
#6m : "2015/03/01","2015/08/31"
#3m : "2015/06/01","2015/08/31"

winning24m = get_winning_data("2013/04/01","2015/04/30")
winning12m = get_winning_data("2014/04/01","2015/04/30")
winning6m = get_winning_data("2014/11/01","2015/04/30")
winning3m = get_winning_data("2015/02/01","2015/04/30")

## ========== PRINTING OUT THE RESUTLS ========== ##

print "winning24m i24"
print "==============="
print winning24m[0]
print

print "winning12m i24"
print "==============="
print winning12m[0]
print

print "winning6m i24"
print "==============="
print winning6m[0]
print

print "winning3m i24"
print "==============="
print winning3m[0]
print

print "=================================================="
print "==================================================\n"

print "winning24m i12"
print "==============="
print winning24m[1]
print

print "winning12m i12"
print "==============="
print winning12m[1]
print

print "winning6m i12"
print "==============="
print winning6m[1]
print

print "winning3m i12"
print "==============="
print winning3m[1]
print
print "=================================================="
print "==================================================\n"

print "winning24m i6"
print "==============="
print winning24m[2]
print

print "winning12m i6"
print "==============="
print winning12m[2]
print

print "winning6m i6"
print "==============="
print winning6m[2]
print

print "winning3m i6"
print "==============="
print winning3m[2]
print
print "=================================================="
print "==================================================\n"

print "winning24m i4"
print "==============="
print winning24m[3]
print

print "winning12m i4"
print "==============="
print winning12m[3]
print

print "winning6m i4"
print "==============="
print winning6m[3]
print

print "winning3m i4"
print "==============="
print winning3m[3]
print

print "========== EXECUTION COMPLETED =========="

