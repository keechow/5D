"""
Name:       parsing_module3.py
Objective:  Same with parsing_module.py but date range entered as params Return a list containing 4D numbers and its occurrences according to prize category
Params:     correctly formatted date. type<str>
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

def string_stripper(input_string):
    #strip unwanted characters from data parsed
    return input_string[3:-2]

def get_data(date):
    #2015/01/31
    year = date[:4]
    month = date[5:7]
    day = date[8:]
    start_year = "startyear=" + year  + "&"
    start_month = "startmonth=" + month + "&"
    start_day = "startday=" + day + "&"
    end_year = "endyear=" + year + "&"
    end_month = "endmonth=" + month + "&"
    end_day = "endday=" + day

    parent_address = "http://my.myfreepost.com/en/damacai/4d/frequency/?"
    query_address = parent_address + start_year + start_month + start_day + end_year + end_month + end_day

 
    # lists to hold numbers and their respective occurrences according to prize categories
    num_list = []
    num_total = []
    num_top3 = []
    num_1st = []
    num_2nd = []
    num_3rd = []
    num_starter = []
    num_conso = []

    soup = BeautifulSoup(urllib2.urlopen(query_address), 'lxml')    

    soup_table_row = soup('table')[0].findAll('tr')         #look for table rows in data table

    counter = 1
    while counter < len(soup_table_row):
        num_data = string_stripper(repr(soup_table_row[counter].findAll('td')[0].a.contents))
        num_list.append(num_data[:4])                                       

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

def print_each(lst):
    for each in lst:
        print each

## Below are codes for testing
"""
print get_data("2015/09/01")
"""

        
