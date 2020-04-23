#!/usr/bin/python3
print("Enter two numbers and their additions \n")
m = int(input("Enter value of m : "))
n = int(input("Enter value of n: "))
s = 0
while(m <= n):
    s = s + m
    m = m + 1
print("Sum : " ,s)
