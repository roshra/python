#!/usr/local/bin/python3

ch = input("Enter a character or number : ")
if(ch >= 'A' and ch <='Z'):
    print("Upper case character")
elif (ch >= 'a' and ch <= 'b'):
    print("Lower case character")
elif (ch >='0' and ch <= '9'):
    print("a number was entered")
