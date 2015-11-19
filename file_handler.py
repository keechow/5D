"""
Name: file_handler.py
Objective: write and read from file
Params: list of strings
Author: The Echo Telion Project <echo.telion@gmail.com>

"""
import time

def write_to(list_input):
    file_name = raw_input("Please enter file name\n")

    if len(file_name) == 0:
        sys_time = time.strftime("%c")        #get sys time in format:- 
        ys_time = sys_time.replace("/","")        #09/05/15 16:51:05
        s_time = ys_time.replace(":","")        #strip away all unwanted char
        _time = s_time.replace(" ","_")      #now:- 090515_165105 => use as filename
        file_name = _time + ".txt"
    else:
        file_name += ".txt"
    
    txt_file = open(file_name, "w")
    for each_line in list_input:
        txt_file.write(each_line)
        txt_file.write("\n")
    
    txt_file.close()
    
    
def read_from(file_name):
    # read str data from txt file
    # return a list with element type<list>
    # each element is similar to combined result list element
    
    return_list = []
    txt_file = open(file_name, "r")
    data = txt_file.read()
    s_data= data.split("\n")
            #split data at \n and return as list

    for each in s_data:
        new = []
        new.append(each[:4])        #1st char = 4 digit num
        try:
            for i in range(4,11):
                new.append(int(each[i]))
        except:
            continue        # try except used to ignore the final empty line in our data txt file
        return_list.append(new)
    return return_list
    

#Below are codes for testing purposes
"""
from parsing_module import print_each
from parsing_module import get_data
from combine_module import str_combine

raw_result = get_data()
combined_result = str_combine(raw_result)
write(combined_result)
read_list = read("3.txt")

print"hahahha"
print
print_each(read_list)

print "========== end =========="
"""




    
