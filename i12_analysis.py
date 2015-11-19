"""
Name: i12_analysis.py
Objective: Analyze i12 num
Method:     separate() - Break list of i12 num into different list according to double digit
                Params: i12 combined_result 
                Return: list with 10 elements, containing i12_combine_result sorted into respective double digits

                identify() - Identify the prevalent single digit paired with double digits in i12 numbers
                Params: separated i12 combined result list
                Return: a list of sorted numbers with the most prevalent digit at front

                
Author: The Echo Telion Project <echo.telion@gmail.com>

"""

def separate(i12_combined_result_list):        
    zero = []
    one = []
    two = []
    three = []
    four = []
    five = []
    six = []
    seven = []
    eight = []
    nine = []
    
    digit = [("0",zero),("1",one),("2",two),("3",three),("4",four),("5",five),("6",six),("7",seven),("8",eight),("9",nine)]

    
           
    for each_element in i12_combined_result_list:           #element type<list>
        for each_digit in digit:                     #check against each digit 0 to 9
                if each_element[0].count(each_digit[0]) == 2:      #if check digit count == 2
                    each_digit[1].append(each_element)          #append element to list inside digit

    return_list = []
    for each in digit:
        return_list.append(each[1])

    return return_list

def identify(separated_i12_combined_result_list):
    zero = []
    one = []
    two = []
    three = []
    four = []
    five = []
    six = []
    seven = []
    eight = []
    nine = []
    
    digit = [("0",zero),("1",one),("2",two),("3",three),("4",four),("5",five),("6",six),("7",seven),("8",eight),("9",nine)]

    for each in separated_i12_combined_result_list:        # start testing each element in given list
        for each_digit in digit:                            #test it against each digit
            if each[0].count(each_digit[0]) == 1:            #check if element contain current test digit. we want 1 occurrence only. 2 means it is the double digit
                each_digit[1].append(each)
    
    return_list = []
    for each in digit:
        return_list.append(each[1])
    return return_list



## Below are testing code
"""
from parsing_module import get_data
from parsing_module import print_each
from combine_module import combine
import num_cat_sort_module
from sorting_module import sort

result_12m_raw = get_data()
print "Data retrieved from web page"
result_12m_combine = combine(result_12m_raw)
print "Raw data combined"
i12_12m = num_cat_sort_module.get_i12(result_12m_combine)
print "i12 num extracted"

i12_12m_TOP3 = sort(i12_12m, 2)
print "i12 num sorted for TOP3"

i12_12m_TOP3_separated = separate(i12_12m_TOP3[:50])

print_each(identify(i12_12m_TOP3_separated[0]))
            
"""
