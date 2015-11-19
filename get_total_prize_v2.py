"""
Name: get_total_winning.py
Objective: calculate total prize won by i12 num for the past 24 months
Author: The Echo Telion Project <echo.telion@gmail.com>

"""
from parsing_module import print_each
from parsing_module4 import get_data
from combine_module import str_combine
from combine_module import combine
import num_cat_sort_module
    #get_i24, get_i12, get_i6, get_i4, get_i1
    #get_all_result : [[i24],[i12],[i6],[i4],[i1]]
from sorting_module import sort
        # sort(combined_result, prize_cat)
        # 0 = number,    1 = Total,      2 = Top3
        # 3 = 1st Prize, 4 = 2nd Prize,  5 = 3rd Prize
        # 6 = Starter,   7 = Consolation

import prize_calc

class Calc_prize(object):
	def __init__(self):
		self.result_raw = []
		self.result_combined = []
		
		main()
		
	def get_result_raw(self):
		return self.result_raw
		
	def get_result_combined(self):
	    return self.result_combined

## ========== PARSE DATA FROM WEB PAGE ========= ##
	def parse_data(self):
	 ## ===== WEB PARSING STAGE ===== ##
		
		print "result_24m : 2013/09/01 to 2013/09/30\n"
		result_24m_raw = get_data("2013/09/01", "2013/09/30")

		print "result_23m : 2013/10/01 to 2013/10/31\n"
		result_23m_raw = get_data("2013/10/01", "2013/10/31")

		print "result_22m : 2013/11/01 to 2013/11/30\n"
		result_22m_raw = get_data("2013/11/01", "2013/11/30")

		print "result_21m : 2013/12/01 to 2013/12/31\n"
		result_21m_raw = get_data("2013/12/01", "2013/12/31")

		print "result_20m : 2014/01/01 to 2014/01/31\n"
		result_20m_raw = get_data("2014/01/01", "2014/01/31")

		print "result_19m : 2014/02/01 to 2014/02/28\n"
		result_19m_raw = get_data("2014/02/01", "2014/02/28")

		print "result_18m : 2014/03/01 to 2014/03/31\n"
		result_18m_raw = get_data("2014/03/01", "2014/03/31")

		print "result_17m : 2014/04/01 to 2014/04/30\n"
		result_17m_raw = get_data("2014/04/01", "2014/04/30")

		print "result_16m : 2014/05/01 to 2014/05/31\n"
		result_16m_raw = get_data("2014/05/01", "2014/05/31")

		print "result_15m : 2014/06/01 to 2014/06/30\n"
		result_15m_raw = get_data("2014/06/01", "2014/06/30")

		print "result_14m : 2014/07/01 to 2014/07/31\n"
		result_14m_raw = get_data("2014/07/01", "2014/07/31")

		print "result_13m : 2014/08/01 to 2014/08/31\n"
		result_13m_raw = get_data("2014/08/01", "2014/08/31")

		print "result_12m : 2014/09/01 to 2014/09/30\n"
		result_12m_raw = get_data("2014/09/01", "2014/09/30")

		print "result_11m : 2014/10/01 to 2014/10/31\n"
		result_11m_raw = get_data("2014/10/01", "2014/10/31")

		print "result_10m : 2014/11/01 to 2014/11/30\n"
		result_10m_raw = get_data("2014/11/01", "2014/11/30")

		print "result_9m : 2014/12/01 to 2014/12/31\n"
		result_9m_raw = get_data("2014/12/01", "2014/12/31")

		print "result_8m : 2015/01/01 to 2015/01/31\n"
		result_8m_raw = get_data("2015/01/01", "2015/01/31")

		print "result_7m : 2015/02/01 to 2015/02/28\n"
		result_7m_raw = get_data("2015/02/01", "2015/02/28")

		print "result_6m : 2015/03/01 to 2015/03/31\n"
		result_6m_raw = get_data("2015/03/01", "2015/03/31")

		print "result_5m : 2015/04/01 to 2015/04/30\n"
		result_5m_raw = get_data("2015/04/01", "2015/04/30")

		print "result_4m : 2015/05/01 to 2015/05/31\n"
		result_4m_raw = get_data("2015/05/01", "2015/05/31")

		print "result_3m : 2015/06/01 to 2015/06/30\n"
		result_3m_raw = get_data("2015/06/01", "2015/06/30")

		print "result_2m : 2015/07/01 to 2015/07/31\n"
		result_2m_raw = get_data("2015/07/01", "2015/07/31")

		print "result_1m : 2015/08/01 to 2015/08/31\n"
		result_1m_raw = get_data("2015/08/01", "2015/08/31")

		result_raw = [result_24m_raw,result_23m_raw,result_22m_raw,result_21m_raw,result_20m_raw,
					  result_19m_raw,result_18m_raw,result_17m_raw,result_16m_raw,result_15m_raw,
					  result_14m_raw,result_13m_raw,result_12m_raw,result_11m_raw,result_10m_raw,
					  result_9m_raw,result_8m_raw,result_7m_raw,result_6m_raw,result_5m_raw,
					  result_4m_raw,result_3m_raw,result_2m_raw,result_1m_raw]
					  
		set_result_raw(result_raw)

# ========== NUMBER ANALYSIS SEGMENT ========== #
    def combine_result(self):
	    # combine raw result into a list containing combined result for all num cat
	    for each in self.result_raw:
			new = combine(each)
			self.result_combined.append(new)
			
	def get_i24_combined(self):
		#return list containing combined result for i24
		i24 = []
		for each in self.result_combined:
			new =  num_cat_sort_module.get_i24(each)
			i24.append(new)
		return i24
	
	def get_i12_combined(self):
		#return list containing combined result for i12
		i12 = []
		for each in self.result_combined:
			new =  num_cat_sort_module.get_i12(each)
			i12.append(new)
		return i12
	
	def get_i6_combined(self):
		#return list containing combined result for i6
		i6 = []
		for each in self.result_combined:
			new =  num_cat_sort_module.get_i6(each)
			i6.append(new)
		return i6
	
	def get_i4_combined(self):
		#return list containing combined result for i4
		i4 = []
		for each in self.result_combined:
			new =  num_cat_sort_module.get_i4(each)
			i4.append(new)
		return i4

	def get_i24_monthly_winning(self):		
		# return list of monthly winning for i24
		monthly_winning = []
		for each_month in get_i24_combined():
			this_month_winning = 0
			for each_draw in each_month:
				this_month_winning += prize_calc.i24_prize_calc(each_draw)
			monthly_winning.append(this_month_winning)
		return i24_monthly_winning
		
	def get_i12_monthly_winning(self):		
		# return monthly winning for i12
		monthly_winning = []
		for each_month in get_i12_combined():
			this_month_winning = 0
			for each_draw in each_month:
				this_month_winning += prize_calc.i12_prize_calc(each_draw)
			monthly_winning.append(this_month_winning)
		return monthly_winning		
		
	def get_i6_monthly_winning(self):		
		# return monthly winning for i6
		monthly_winning = []
		for each_month in get_i6_combined():
			this_month_winning = 0
			for each_draw in each_month:
				this_month_winning += prize_calc.i6_prize_calc(each_draw)
			monthly_winning.append(this_month_winning)
		return monthly_winning		
		
	def get_i4_monthly_winning(self):		
		# return monthly winning for i4
		monthly_winning = []
		for each_month in get_i4_combined():
			this_month_winning = 0
			for each_draw in each_month:
				this_month_winning += prize_calc.i4_prize_calc(each_draw)
			monthly_winning.append(this_month_winning)
		return monthly_winning		
		

		i24_total_winning = 0
		for each in i24_monthly_winning:
			i24_total_winning += each
			
		i12_monthly_winning = []
		for each_month in i12:
			this_month_winning = 0
			for each_draw in each_month:
				this_month_winning += prize_calc.i12_prize_calc(each_draw)
			i12_monthly_winning.append(this_month_winning)
		i12_total_winning = 0
		for each in i12_monthly_winning:
			i12_total_winning += each

		i6_monthly_winning = []
		for each_month in i6:
			this_month_winning = 0
			for each_draw in each_month:
				this_month_winning += prize_calc.i6_prize_calc(each_draw)
			i6_monthly_winning.append(this_month_winning)
		i6_total_winning = 0
		for each in i6_monthly_winning:
			i6_total_winning += each
			
		i4_monthly_winning = []
		for each_month in i4:
			this_month_winning = 0
			for each_draw in each_month:
				this_month_winning += prize_calc.i4_prize_calc(each_draw)
			i4_monthly_winning.append(this_month_winning)
		i4_total_winning = 0
		for each in i4_monthly_winning:
			i4_total_winning += each

	def get_num_of_draw(self):
	    #Calculate number of draw for the past 24 months
		all_draw_count = []
		for each_month in self.result_combined:
			monthly_draw_count = 0
			for each_draw in each_month:
				monthly_draw_count += each_draw[3]
			all_draw_count.append(monthly_draw_count)    
		total_draw_count = 0
		for each_month in all_draw_count:
			total_draw_count += each_month
		return total_draw_count
	
	def main(self):
		parse_data()
		combine_result()
		
		# Calculate return amount and return rate   
i24_inv = total_draw_count * 210      #210 group of i24 num
i12_inv = total_draw_count * 360        #360 group of i12 num
i6_inv = total_draw_count * 45        #45 group of i6 num
i4_inv = total_draw_count * 90        #90 group of i4 num

i24_return = i24_total_winning - i24_inv
i12_return = i12_total_winning - i12_inv
i6_return = i6_total_winning - i6_inv
i4_return = i4_total_winning - i4_inv

i24_return_percent = (float(i24_return) / i24_inv) * 100.0
i12_return_percent = (float(i12_return) / i12_inv) * 100.0
i6_return_percent = (float(i6_return) / i6_inv) * 100.0
i4_return_percent = (float(i4_return) / i4_inv) * 100.0

    # Pass combined result list to get prize cat count
i24_prize_cat_count = []
for each_month in i24:
    count = prize_calc.calc_prize_cat(each_month)
    i24_prize_cat_count.append(count)
    
i12_prize_cat_count = []
for each_month in i12:
    count = prize_calc.calc_prize_cat(each_month)
    i12_prize_cat_count.append(count)

i6_prize_cat_count = []
for each_month in i6:
    count = prize_calc.calc_prize_cat(each_month)
    i6_prize_cat_count.append(count)

i4_prize_cat_count = []
for each_month in i4:
    count = prize_calc.calc_prize_cat(each_month)
    i4_prize_cat_count.append(count)




## ===== Printing out result ===== ##
counter = 24
print "\nPrize cat count for i24"
for each in i24_prize_cat_count:
    print str(counter) + " - " + str(each)
    counter -= 1

counter = 24
print "\nPrize cat count for i12"
for each in i12_prize_cat_count:
    print str(counter) + " - " + str(each)
    counter -= 1

counter = 24
print "\nPrize cat count for i6"
for each in i6_prize_cat_count:
    print str(counter) + " - " + str(each)
    counter -= 1

counter = 24
print "\nPrize cat count for i4"
for each in i4_prize_cat_count:
    print str(counter) + " - " + str(each)
    counter -= 1


"""
print "Total draw: " + str(total_draw_count)
print
print "Total winning i24: " + str(i24_total_winning)
print "Total winning i12: " + str(i12_total_winning)
print "Total winning i6: " + str(i6_total_winning)
print "Total winning i4: " + str(i4_total_winning)
print
print "Total i24 investment: " + str(i24_inv)
print "Total i12 investment: " + str(i12_inv)
print "Total i6 investment: " + str(i6_inv)
print "Total i4 investment: " + str(i4_inv)
print
print "Total i24 return: " + str(i24_return)
print "Percentage: " + str(i24_return_percent)
print
print "Total i12 return: " + str(i12_return)
print "Percentage: " + str(i12_return_percent)
print
print "Total i6 return: " + str(i6_return)
print "Percentage: " + str(i6_return_percent)
print
print "Total i4 return: " + str(i4_return)
print "Percentage: " + str(i4_return_percent)
print

counter = 24
print "i24 MONTHLY EARNINGS" 
for each in i24_monthly_winning:
    print str(counter) + " : " + str(each)
    counter -= 1

counter = 24
print "i12 MONTHLY EARNINGS" 
for each in i12_monthly_winning:
    print str(counter) + " : " + str(each)
    counter -= 1

counter = 24
print "i6 MONTHLY EARNINGS" 
for each in i6_monthly_winning:
    print str(counter) + " : " + str(each)
    counter -= 1

counter = 24
print "i4 MONTHLY EARNINGS" 
for each in i4_monthly_winning:
    print str(counter) + " : " + str(each)
    counter -= 1
"""
print "========== END OF EXECUTION =========="
