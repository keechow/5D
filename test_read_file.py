from parsing_module import print_each
from num_cat_sort_module import get_i12

from file_handler import read_from

from sorting_module import sort
        #example of result_list element: ['1008',3,2,1,0,1,0,1]

file_name = "2014_sat_all.txt"

data_file = open(file_name, "r")
data = data_file.read()
s_data = data.split("\n")

return_list = []
counter = 0
for each in s_data:
    counter += 1
    new_el = []
    new_el.append(each[:4])
    try:
        for i in range(4,11):
            new_el.append(int(each[i]))
    except:
        print "========== ERROR =========="
        print "Error at line: ", counter
        print "========================="
        continue
    return_list.append(new_el)

print len(return_list)


