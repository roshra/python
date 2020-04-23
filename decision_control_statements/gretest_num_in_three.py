#!/usr/local/bin/python3
# find greatest num in three numbers
# instatiate empty list
# extend list 
# compare each number against other two

num_list = []
num0 = int(input("enter first number : "))
num1 = int(input("enter sec number : "))
num2 = int(input("enter third number : "))
num_list.extend([num0,num1,num2])
print(num_list)
if((num_list[0] > num_list[1]) and (num_list[0] > num_list[2])):
    print("number {num0} is greatest".format(num0=num_list[0]))
elif((num_list[1] > num_list[0]) and (num_list[1] > num_list[2])):
    print("number {num1} is greatest".format(num1=num_list[1]))
else:
    print("number {num2} is greatest".format(num2=num_list[2]))
    
