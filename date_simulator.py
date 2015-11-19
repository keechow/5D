"""
Name: date_simulator.py
Objective: Produce dates for Wednesday, Saturday and Sunday
Params: year, month

Author: The Echo Telion Project <echo.telion@gmail.com>

"""
import calendar


def simulate_date (year, month):
    wed_date = []
    sat_date = []
    sun_date = []
    
    limit = calendar.monthrange(year, month)
    start_weekday = limit[0]
    end_date = limit[1]
    current_date = 1

    while current_date <= end_date:
        if start_weekday > 6:
            start_weekday = 0        # this is to reset weekday back to Monday
        elif start_weekday == 2:
            wed_date.append(current_date)
        elif start_weekday == 5:
            sat_date.append(current_date)
        elif start_weekday == 6:
            sun_date.append(current_date)

        start_weekday += 1
        current_date += 1

    return [wed_date, sat_date, sun_date]

def get_wed (year, month):
    result = simulate_date(year, month)
    return result[0]

def get_sat (year, month):
    result = simulate_date(year, month)
    return result[1]

def get_sun (year, month):
    result = simulate_date(year, month)
    return result[2]

def add0 (num):
    str_num  = str(num)
    if len(str_num) < 2:
        return ("0" + str_num)
    else:
        return str_num
    
def date (year, month, day):
    return (str(year) + "/" + add0(month) + "/" + add0(day))
    
def date_creator(year, month):

    wed = get_wed(year, month)
    sat = get_sat(year, month)
    sun = get_sun(year, month)

    wed_date = []
    sat_date = []
    sun_date = []

    for each in wed:
        wed_date.append(date(year, month, each))
    for each in sat:
        sat_date.append(date(year, month, each))
    for each in sun:
        sun_date.append(date(year, month, each))

    return [wed_date, sat_date, sun_date]



    
    
