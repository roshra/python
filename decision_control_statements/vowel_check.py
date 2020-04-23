#!/usr/local/bin/python3
# Enter character and check if its vowel
# I implemented a list here which comprises of all vowels 

ch = raw_input("Enter the char : ")
vowels = ["a","e","i","o","u"]
ch = ch.lower()
for word in vowels:
    if( word == ch):
        print("{} is a vowel".format(ch))
        exit()
    else:
        print("{word} in Vowel list did not match with {ch}".format(word = word, ch = ch))


