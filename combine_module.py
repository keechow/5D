"""
Name: combine_module.py
Objective: Take result and restructure. Each element has num and its occurrences count
Params: result list
Return: restructured list with num and occurences count as one element
Author: The Echo Telion Project <echo.telion@gmail.com>

"""

def combine(result_list):
    return_list = []
    counter = 0

    for each in result_list[0]:        #this is the number of num in result_list
        new_element = []
        new_element.append(each)
        for i in range(7):        #take element 1 to 7 from result_list - occurrences
            new_element.append(result_list[i+1][counter])
        return_list.append(new_element)
        counter += 1

    return return_list

def str_combine(result_list):
    # function same as combine but return list containing result in type<str>
    return_list = []
    counter = 0

    for each in result_list[0]:
        new_element = ""
        new_element += str(each)
        for i in range(7):
            new_element += str(result_list[i+1][counter])
        return_list.append(new_element)
        counter += 1

    return return_list

# Below are testing codes
"""
from parsing_module import get_data
from parsing_module import print_each
raw_result = get_data()
str_result = str_combine(raw_result)
print_each(str_result)
"""



            
        
