#Args is for functions, argv is for CMDLine arguments
#Also, *args means take arbitrary amount of arguments
def print_two(*args):
#Assign arg1 and arg2 to args
    arg1, arg2 = args
    print "arg1: %s, arg2: %s" %(arg1, arg2)

#The above func can also be written without *args
def print_two_again(arg1, arg2):
    print "arg1: %s, arg2:%s" %(arg1, arg2)

#Function that takes only one argument
def print_one(arg1):
    print "arg1:%s" %arg1

#Function that takes no argument
def print_none():
    print "Nothing!!"

print_two("Dilip", "Dwarak")
print_two_again("Pradyumna", "Dwarak")
print_one("Deadly")
print_none()
    