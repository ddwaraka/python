import sys

try:
	print (5/0)
except Exception as e:
	print ("exception: ", type(e), e) #prints type and name of exception

print ("Life goes on")