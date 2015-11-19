"""
Name:       parsing_module.py
Objective:  Let user select a date range to parse 4D number data. Return a list containing 4D numbers and its occurrences according to prize category
Params:     None
Return:      A list containing 8 list elements.
                Element 0: list of 4D number.
                Element 1: list of occurrences for all prize category
                Element 2: list of occurences for Top 3 prizes
                Element 3: list of occurences for 1st prize
                Element 4: list of occurences for 2nd prize
                Element 5: list of occurences for 3rd prize
                Element 6: list of occurences for Starter prize
                Element 7: list of occurences for Consolation prize
Author:     Project Echo Telion [echo.telion@gmail.com]

"""

from bs4 import BeautifulSoup
import urllib2
import time

user_start_date = ""
user_end_date = ""

def set_data_range():
    
    #1: Get user to enter the date range for data wanted. (Start date and end date)
    #2: Break user input into start year, month, day and end year, month day
    #3: Concatenate user input with parent address to form full query address
    #4: return the full query address
    current_date = time.strftime("%d/%m/%Y")
    global user_start_date
    global user_end_date
    user_start_date = raw_input("Please enter start date (yyyy/mm/dd)\n")
    user_end_date = raw_input("Please enter end date (yyyy/mm/dd)\n")

    # if user did not enter anything, start date will be 1996/01/01 and
    # end date will be current date
    if len(user_start_date) == 0:
        user_start_date = "1996/01/01"
    if len(user_end_date) == 0:
        user_end_date = time.strftime("%Y/%m/%d")

    print "Begin date: " + user_start_date
    print "End date: " + user_end_date

    
    start_year = "startyear=" + user_start_date[0:4] + "&"
    start_month = "startmonth=" + user_start_date[5:7] + "&"
    start_day = "startday=" + user_start_date[8:] + "&"
    end_year = "endyear=" + user_end_date[0:4] + "&"
    end_month = "endmonth=" + user_end_date[5:7] + "&"
    end_day = "endday=" + user_end_date[8:]

    parent_address = "http://my.myfreepost.com/en/damacai/4d/frequency/?"
    return parent_address + start_year + start_month + start_day + end_year + end_month + end_day

def string_stripper(input_string):
    #strip unwanted characters from data parsed
    return input_string[3:-2]

def get_data():
    # lists to hold numbers and their respective occurrences according to prize categories
    num_list = []
    num_total = []
    num_top3 = []
    num_1st = []
    num_2nd = []
    num_3rd = []
    num_starter = []
    num_conso = []

    soup = BeautifulSoup(urllib2.urlopen(set_data_range()), 'lxml')    

    soup_table_row = soup('table')[0].findAll('tr')         #look for table rows in data table

    counter = 1
    while counter < len(soup_table_row):
        num_data = string_stripper(repr(soup_table_row[counter].findAll('td')[0].a.contents))
        num_list.append(num_data[:4])                                       

        #num_list.append(string_stripper(repr(soup_table_row[counter].findAll('td')[0].a.contents)))          
        num_total.append(int(string_stripper(repr(soup_table_row[counter].findAll('td')[1].contents))))          #total occurence for number
        num_top3.append(int(string_stripper(repr(soup_table_row[counter].findAll('td')[2].contents))))          # top3 occurence for number
        num_1st.append(int(string_stripper(repr(soup_table_row[counter].findAll('td')[3].contents))))            #1st prize occurence
        num_2nd.append(int(string_stripper(repr(soup_table_row[counter].findAll('td')[4].contents))))           #2nd prize occurence
        num_3rd.append(int(string_stripper(repr(soup_table_row[counter].findAll('td')[5].contents))))            #3rd prize occurence
        num_starter.append(int(string_stripper(repr(soup_table_row[counter].findAll('td')[6].contents))))       #starter prize occurence
        num_conso.append(int(string_stripper(repr(soup_table_row[counter].findAll('td')[7].contents))))        #consolation prize occurence
        counter += 1

    return_list = []
    return_list.append(num_list)
    return_list.append(num_total)
    return_list.append(num_top3)
    return_list.append(num_1st)
    return_list.append(num_2nd)
    return_list.append(num_3rd)
    return_list.append(num_starter)
    return_list.append(num_conso)

    return return_list

def get_date():
    # return date range specified by user. e.g.: "1996.01.01 to 2015.01.31"
    start_date = user_start_date[0:4] + "." + user_start_date[5:7] + "." + user_start_date[8:]
    end_date = user_end_date[0:4] + "." + user_end_date[5:7] + "." + user_end_date[8:]

    return start_date + "_to_" + end_date

def print_each(lst):
    for each in lst:
        print each


## ===== Below are codes for testing ===== ##

raw_result = get_data()
print "========== END OF EXECUTION ========="

