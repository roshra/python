mluvufile = "/Documents/MluCli_exe_poll_-lu.txt"
out1 = open(mluvufile,"r")

# this one reads entire file
#print (out1.read())

# How to read file line by line - replace with line number and it will print only that line
out2 = out1.readlines()
for x in out2:
    print(x)

