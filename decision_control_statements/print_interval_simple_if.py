#!/user/local/bin/python3
# takes input of integer, find its range and prints using simple if statement

num = int (input("enter a number to find its range: "))
if(num > 0 and num <=10):
    print("{} is in range 0-10".format(num))

if(num > 10 and num <=20):
    print("{} is in range 0-10".format(num))

if(num > 20 and num <=30):
    print("{} is in range 0-10".format(num))

if(num > 30):
    print("{} is greater than 30 and not allowed". format(num))
    exit()

