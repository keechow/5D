"""
Name: sorting_module.py
Objective: Take in a list of num and its occurrences. Sort according the highest occurencces
Params: result_list, prize_cat
Return: List of sorted num with highest to lowest occurrence, based on prize_cat
Author: The Echo Telion Project <echo.telion@gmail.com>

"""

#example of result_list element: ['1008',3,2,1,0,1,0,1]
#translates to number 1008 drawn total 3 times. 2 times in TOP3. 1st prize - 1,
# 2nd prize - 0, 3rd prize - 1, Started - 0, Conso - 1
# Pos 0: Number
# Pos 1: Total
# Pos 2: Top3
# Pos 3: 1st
# Pos 4: 2nd
# Pos 5: 3rd
# Pos 6: Starter
# Pos 7: Consolation

from operator import itemgetter
def sort(result_list, prize_cat):
       return sorted(result_list, key=itemgetter(prize_cat), reverse=True)
