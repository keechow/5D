"""
Name: prize_calc.py
Objective: Calculate prize won by a number
Params: combined_result element
Return: prize amount
Author: The Echo Telion Project <echo.telion@gmail.com>
"""
def i24_prize_calc(combined_result_element):
    # 1st   105
    # 2nd   42
    # 3rd   21
    # Starter   8
    # Conso 3

    #['1123',Total,TOP3,1st,2nd,3rd,Starter,Conso]
    prize_list = [105,42,21,8,3]

    counter = 3
    total_prize = 0
    while counter < len(combined_result_element):        #prize count are at idx 3:8
        total_prize += (combined_result_element[counter] * prize_list[counter - 3])  #offset 3 idx because first 3 element not prize count
        counter += 1
    return total_prize


def i12_prize_calc(combined_result_element):
    # 1st   209
    # 2nd   84
    # 3rd   42
    # Starter   15
    # Conso 5

    #['1123',Total,TOP3,1st,2nd,3rd,Starter,Conso]
    prize_list = [209,84,42,15,5]

    counter = 3
    total_prize = 0
    while counter < len(combined_result_element):        #prize count are at idx 3:8
        total_prize += (combined_result_element[counter] * prize_list[counter - 3])  #offset 3 idx because first 3 element not prize count
        counter += 1

    return total_prize

def i6_prize_calc(combined_result_element):
    # 1st   417
    # 2nd   167
    # 3rd   84
    # Starter   30
    # Conso 10

    #['1123',Total,TOP3,1st,2nd,3rd,Starter,Conso]
    prize_list = [417,167,84,30,10]

    counter = 3
    total_prize = 0
    while counter < len(combined_result_element):        #prize count are at idx 3:8
        total_prize += (combined_result_element[counter] * prize_list[counter - 3])  #offset 3 idx because first 3 element not prize count
        counter += 1

    return total_prize

def i4_prize_calc(combined_result_element):
    # 1st   625
    # 2nd   250
    # 3rd   125
    # Starter   45
    # Conso 15

    #['1123',Total,TOP3,1st,2nd,3rd,Starter,Conso]
    prize_list = [625,250,125,45,15]

    counter = 3
    total_prize = 0
    while counter < len(combined_result_element):        #prize count are at idx 3:8
        total_prize += (combined_result_element[counter] * prize_list[counter - 3])  #offset 3 idx because first 3 element not prize count
        counter += 1

    return total_prize

def calc_prize_cat(combined_result_list):
    top3 = 0
    first = 0
    second = 0
    third = 0
    starter = 0
    conso = 0
    result_list = [top3,first,second,third,starter,conso]
    for each in combined_result_list:
        counter = 0
        while counter < len(result_list):
            result_list[counter] += each[counter + 2]
            counter += 1
    return result_list
     
        


## Below are codes for testing ##
"""
result = [['1123',3,3,2,1,0,0,0],['1124',2,1,1,0,0,1,0], ['1125',1,0,0,0,0,1,0]]
print calc_prize_cat(result)
"""
           
