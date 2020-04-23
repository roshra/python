#!/usr/local/bin/python3
#Find larger of two numbers 

num1 = int (input("Enter first number : "))
num2 = int (input("Enter second number: "))
if (num1 > num2):
    print("{num1} is greater than {num2}".format(num1=num1, num2=num2))
else:
    print("{num2} is greater than {num1}".format(num2=num2, num1=num1))
