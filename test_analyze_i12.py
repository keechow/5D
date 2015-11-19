from file_handler import read_from
from parsing_module import print_each
from num_cat_sort_module import num_cat_sorter
from sorting_module import sort
file_name = "2014_sat_all.txt"

data_file = read_from(file_name)

num_i12 = num_cat_sorter(data_file, 2)

num_i12_sort_top3 = sort(num_i12,2)

top50_i12_top3 = num_i12_sort_top3[:-5]

print_each(top50_i12_top3)
