print 40.0178827+40.871829

f=22.0; b=7.0
c=f/b
print "When you divide %d with %d and print it, you get %d"%(f,b,c)


formatter = "%r %r %r %r"
print formatter % (1,2,3,4)
mythings = "hello", "hi", "good", 1, 2
a=mythings[0]
mythings2="Jan\nFeb\nMarch\nApril\nMay\nJune"
print a+ " hi"
print mythings2

try:
    input = raw_input
except NameError:
    pass

person=input("Enter a name!")
print ("hi"+person)