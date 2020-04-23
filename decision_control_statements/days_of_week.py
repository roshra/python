#!/usr/local/bin/python3
import re
# python dict, key value pair
# i spend a lot of time on this code by doing a mistake 
# the mistake was, that while creating a dict , i wrapped the key value in double quotes 
# there by wasting a lot of time in getting this right post that 

days_dict = {
1:"sunday",
2:"monday",
3:"tuesday",
4:"wednesday",
5:"thursday",
6:"friday",
7:"saterday"
}
num = int(input("Enter number between 1-7 to know day of week:"))
#num_modified = '"{}"'.format(num)
#num_modified.split()
#print(num_modified)
print(days_dict[num])
