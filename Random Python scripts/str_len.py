#Program to calculate length of a string without using len
import os
global strlen
strlen = 0
def length(string):
    for i in string:
        if i=="":
            break
        else:
            global strlen
            strlen+=1
    return strlen

l = length ("dilip is good")
print l