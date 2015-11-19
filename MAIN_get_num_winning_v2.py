"""
Name: MAIN_get_num_winning.py
Objective: get winnings for each num for the past 24 months
AUthor: The Echo Telion Project <echo.telion@gmail.com>

"""

from calc_return_given_num_date_range import get_i4win_data as get
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
        
        
print "\n\n\================ BEGIN ======================"
print "================ I-4 ======================"
print "================ YEAR 2014 ======================"
print "================ BEGIN ======================\n\n"
print
print
data_to = "2013-12-31"
result_start = "2014-01-01"
result_end = "2014-01-31"
print "DATA UP TO " + data_to
print "RESULT: " + result_start + " TO " + result_end
print "==============================================="
winning24m = get("2012/01/01",data_to,result_start,result_end)
print "==============================================="
winning12m = get("2013/01/01",data_to,result_start,result_end)
print "==============================================="
winning6m = get("2013/07/01",data_to,result_start,result_end)
print "==============================================="
winning3m = get("2013/10/01",data_to,result_start,result_end)
print "========================================================"
print "========================================================\n\n\n"

data_to = "2014-01-31"
result_start = "2014-02-01"
result_end = "2014-02-28"
print "DATA UP TO " + data_to
print "RESULT: " + result_start + " TO " + result_end
print "==============================================="
winning24m = get("2012/02/01",data_to,result_start,result_end)
print "==============================================="
winning12m = get("2013/02/01",data_to,result_start,result_end)
print "==============================================="
winning6m = get("2013/08/01",data_to,result_start,result_end)
print "==============================================="
winning3m = get("2013/11/01",data_to,result_start,result_end)
print "========================================================"
print "========================================================\n\n\n"

data_to = "2014-02-28"
result_start = "2014-03-01"
result_end = "2014-03-31"
print "DATA UP TO " + data_to
print "RESULT: " + result_start + " TO " + result_end
print "==============================================="
winning24m = get("2012/03/01",data_to,result_start,result_end)
print "==============================================="
winning12m = get("2013/03/01",data_to,result_start,result_end)
print "==============================================="
winning6m = get("2013/09/01",data_to,result_start,result_end)
print "==============================================="
winning3m = get("2013/12/01",data_to,result_start,result_end)
print "========================================================"
print "========================================================\n\n\n"

data_to = "2014-03-31"
result_start = "2014-04-01"
result_end = "2014-04-30"
print "DATA UP TO " + data_to
print "RESULT: " + result_start + " TO " + result_end
print "==============================================="
winning24m = get("2012/04/01",data_to,result_start,result_end)
print "==============================================="
winning12m = get("2013/04/01",data_to,result_start,result_end)
print "==============================================="
winning6m = get("2013/10/01",data_to,result_start,result_end)
print "==============================================="
winning3m = get("2014/01/01",data_to,result_start,result_end)
print "========================================================"
print "========================================================\n\n\n"

data_to = "2014-04-30"
result_start = "2014-05-01"
result_end = "2014-05-31"
print "DATA UP TO " + data_to
print "RESULT: " + result_start + " TO " + result_end
print "==============================================="
winning24m = get("2012/05/01",data_to,result_start,result_end)
print "==============================================="
winning12m = get("2013/05/01",data_to,result_start,result_end)
print "==============================================="
winning6m = get("2013/11/01",data_to,result_start,result_end)
print "==============================================="
winning3m = get("2014/02/01",data_to,result_start,result_end)
print "======================================================="
print "========================================================\n\n\n"

data_to = "2014-05-31"
result_start = "2014-06-01"
result_end = "2014-06-30"
print "DATA UP TO " + data_to
print "RESULT: " + result_start + " TO " + result_end
print "==============================================="
winning24m = get("2012/06/01",data_to,result_start,result_end)
print "==============================================="
winning12m = get("2013/06/01",data_to,result_start,result_end)
print "==============================================="
winning6m = get("2013/12/01",data_to,result_start,result_end)
print "==============================================="
winning3m = get("2014/03/01",data_to,result_start,result_end)
print "========================================================"
print "========================================================\n\n\n"

data_to = "2014-06-30"
result_start = "2014-07-01"
result_end = "2014-07-31"
print "DATA UP TO " + data_to
print "RESULT: " + result_start + " TO " + result_end
print "==============================================="
winning24m = get("2012/07/01",data_to,result_start,result_end)
print "==============================================="
winning12m = get("2013/07/01",data_to,result_start,result_end)
print "==============================================="
winning6m = get("2014/01/01",data_to,result_start,result_end)
print "==============================================="
winning3m = get("2014/04/01",data_to,result_start,result_end)
print "========================================================"
print "========================================================\n\n\n"

data_to = "2014-07-31"
result_start = "2014-08-01"
result_end = "2014-08-31"
print "DATA UP TO " + data_to
print "RESULT: " + result_start + " TO " + result_end
print "==============================================="
winning24m = get("2012/08/01",data_to,result_start,result_end)
print "==============================================="
winning12m = get("2013/08/01",data_to,result_start,result_end)
print "==============================================="
winning6m = get("2014/02/01",data_to,result_start,result_end)
print "==============================================="
winning3m = get("2014/05/01",data_to,result_start,result_end)
print "========================================================"
print "========================================================\n\n\n"


data_to = "2014-08-31"
result_start = "2014-09-01"
result_end = "2014-09-30"
print "DATA UP TO " + data_to
print "RESULT: " + result_start + " TO " + result_end
print "==============================================="
winning24m = get("2012/09/01",data_to,result_start,result_end)
print "==============================================="
winning12m = get("2013/09/01",data_to,result_start,result_end)
print "==============================================="
winning6m = get("2014/03/01",data_to,result_start,result_end)
print "==============================================="
winning3m = get("2014/06/01",data_to,result_start,result_end)
print "========================================================"
print "========================================================\n\n\n"

data_to = "2014-09-30"
result_start = "2014-10-01"
result_end = "2014-10-31"
print "DATA UP TO " + data_to
print "RESULT: " + result_start + " TO " + result_end
print "==============================================="
winning24m = get("2012/10/01",data_to,result_start,result_end)
print "==============================================="
winning12m = get("2013/10/01",data_to,result_start,result_end)
print "==============================================="
winning6m = get("2014/04/01",data_to,result_start,result_end)
print "==============================================="
winning3m = get("2014/07/01",data_to,result_start,result_end)
print "========================================================"
print "========================================================\n\n\n"

data_to = "2014-10-31"
result_start = "2014-11-01"
result_end = "2014-11-30"
print "DATA UP TO " + data_to
print "RESULT: " + result_start + " TO " + result_end
print "==============================================="
winning24m = get("2012/11/01",data_to,result_start,result_end)
print "==============================================="
winning12m = get("2013/11/01",data_to,result_start,result_end)
print "==============================================="
winning6m = get("2014/05/01",data_to,result_start,result_end)
print "==============================================="
winning3m = get("2014/08/01",data_to,result_start,result_end)
print "========================================================"
print "========================================================\n\n\n"

data_to = "2014-11-30"
result_start = "2014-12-01"
result_end = "2014-12-31"
print "DATA UP TO " + data_to
print "RESULT: " + result_start + " TO " + result_end
print "==============================================="
winning24m = get("2012/12/01",data_to,result_start,result_end)
print "==============================================="
winning12m = get("2013/12/01",data_to,result_start,result_end)
print "==============================================="
winning6m = get("2014/06/01",data_to,result_start,result_end)
print "==============================================="
winning3m = get("2014/09/01",data_to,result_start,result_end)
print "========================================================"
print "========================================================\n\n\n"



print "========== EXECUTION COMPLETED =========="

