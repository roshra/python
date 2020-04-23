#!/usr/local/bin/python3
# Take input of year and find if this year is a leap year
year = int(input("Enter the year : "))
if((year%4 == 0 and year%100 != 0) or (year%400 == 0)):
    print("{} is a leap year".format(year))
