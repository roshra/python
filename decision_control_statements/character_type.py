#!/usr/local/bin/python3
# To determine character type input by user

char = input("Enter a character on keyboard: ")
if(char.isalpha()):
    print("is alphabet")
if(char.isdigit()):
    print("is digit")
if(char.isspace()):
    print("user entered a white space character")
