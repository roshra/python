#!/usr/bin/python

# Program to find if user is eligible for voting

age = int(input("Enter your age: "))
if (age >=18):
    print("You are eligible for voting")
else:
    eligiblein_year = 18 - age
    print("You are not eligible now but you would be eligible in {} years".format(eligiblein_year))
    

