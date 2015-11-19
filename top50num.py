"""
Name: Top50Num

Objective: Take a list of 50 numbers. Determine top5 digits.
           Return a list containing numbers from list given that matches
           3 or 4 top5 digits
           
Params:     fifty_num_list - the list of numbers to analyze
            top_digit - number of top digits to analyze
            digit_match - number of digits to match
            
Return:     a list containing nums that has matches top_digit more or equal to digit_match times

Author: echo.telion@gmail.com
"""


def top50num(fifty_num_list, top_digit, digit_match):
    num_value = {"0":0, "1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0,}
    #we use dictionary to save digits occuring in 4D numbers
    
    for each_num in fifty_num_list:        #iterate over each num and count its digits
        for each_digit in each_num:
            if each_digit in num_value:
                num_value[each_digit] += 1
                
    sorted_digits =  sorted(num_value.iteritems(), key=lambda (k,v): (v,k), reverse=True)
    #list containing sorted digits with highest to lowest occurences

    top_digits = []
    for each in sorted_digits[0:top_digit]:
        top_digits.append(each[0])

    matched_num = []

    for each in fifty_num_list:        #run each num and count top5 digit occurences
        counter = 0
        for each_ in top_digits:        
           if each_ in each:
               counter += 1
        if counter >= digit_match:
            matched_num.append(each)

    return matched_num

