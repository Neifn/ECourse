#!/usr/bin/env python3


import calendar
import sys
import datetime
from datetime import date


def create_calendar_page(month=None, year=None):
    if month == None:
        month = datetime.datetime.now().month
    if year == None:
        year = datetime.datetime.now().year
    try:
        month = int(month)
        year = int(year)
    except ValueError:
        print("Please, enter a valid date in format (\'month\', \'year\')")
        sys.exit(0)
    if len(str(year)) > 4 or len(str(month)) > 2 or month < 0 or year < 0 or month > 12:
        print("Please, enter a valid date in format (\'month\', \'year\')")
        sys.exit(0)
    DayStr=""
    Title=[]
    Calendar=[]
    Title.append("--------------------\n")
    Title.append("MO TU WE TH FR SA SU\n")
    Title.append("--------------------\n")
    days_num=calendar.monthrange(year,month)[1]
    for item in range(0,date(year, month, 1).weekday()):
        Calendar.append("  ")
    for day in range(1, days_num+1):
        if day < 10:
            Calendar.append("0"+str(day))
        else:
            Calendar.append(str(day))
    for i in range(len(Calendar)):
        if i != len(Calendar)-1:
            if (i+1) % 7 == 0:
                Calendar[i]+="\n"
            else:
                Calendar[i]+=" "
    for i in Title:
        DayStr+=i
    for i in Calendar:
        DayStr+=i
    return DayStr


print(create_calendar_page(2, 2017))
print(create_calendar_page(1))
print(create_calendar_page())
print(create_calendar_page(3))
print(create_calendar_page("04", "1992"))
