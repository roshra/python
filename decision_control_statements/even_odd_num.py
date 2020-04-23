#!/usr/local/bin/python3

# Program to whether given number is even or odd

num1 = int(input("Enter the number to check if even or odd: "))
check_num = num1%2
if (check_num == 0):
    print("{} is even number".format(num1))
else:
    print("{} is odd number".format(num1))
