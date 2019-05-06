"""Map represents a group of elements in form of key:value pair
dict data typ is example of map
dict represents dictionary
key and value should be seperated by colon
every par should be seperated by comma
all elements shouls be inside curly braces"""

d = {}
d[1] = 'rosh'
d[2] = 'putty'
d[3] = 'camy'
print("printing dictionary d ", d)
print("printing all dictionary keys " , d.keys())
print("printing all dictionary values ", d.values())
del d[1]
print("printing dictionary post deletion of a pair ", d)