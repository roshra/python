#!/usr/bin/python3
import urllib.request
fid=urllib.request.urlopen('https://vibgyor-online.com/vibv1//')
webpage=fid.read().decode('utf-8')
print(webpage)

urllib.request.urlretrieve ("https://vibgyor-online.com/vibv1//", "webpage.html")

# read local file
for line in open('webpage.html'): 
    print(line.strip())
 









