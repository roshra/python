#!/usr/local/bin/python3
# Take input of number, find if number is zero, negative, positive
num = int(input("Enter a number: "))
if(num == 0):
    print("Entered number is zero")
elif(num > 0):
    print("entered number {} is positive number".format(num))
else:
    print("entered number {} is negative".format(num))
