# includes numbers from 0-255 (included) - do not store negative numbers
# This is list of byte numbers
elements = [20,10,0,40]
# convert list into byte array
x = bytes(elements)
print("list now convered to byte array ", x[0])
for i in x: print(i)