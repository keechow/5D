

#read data from txt source
# break long string in txt into 4 list
# draw_date, 1st prize, 2nd prize, 3rd prize

txt_file = open("5D.txt", "r")
data = txt_file.read()
split_data = data.split()

draw_result = split_data[1:]
draw_date = []
prize_1 = []
prize_2 = []
prize_3 = []

for each_line in draw_result:
    split_each_line = each_line.split(",")
    draw_date.append(split_each_line[1])
    prize_1.append(split_each_line[2])
    prize_2.append(split_each_line[3])
    prize_3.append(split_each_line[4])
