#importing argv from sys
from sys import argv
#passing command line arguments, script is name of this python file
#fname is the name of the file we'd like to open!
script, fname = argv

print "we're going to erase %r" %fname
print "To quit out now, Press Ctrl+C"
print "If you're ok with it, Press enter"
raw_input("?")

print "Opening the file"
#'w' stands for write, opening file in write mode
target = open(fname, 'w')

print "Truncating the file. Goodbye!"
#Truncating the file means cleaning it out!
target.truncate()

print "I am now going to ask you to enter 3 lines"
line1 = raw_input("Line1:")
line2 = raw_input("Line2:")
line3 = raw_input("Line3:")


print "I'm going to write these to a file"
#writing line1, line2 and line3 to the file!
target.write("%s\n%s\n%s\n" %(line1, line2, line3))
'''target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")'''


print "And, finally we close it!"
#Closing the file we just operated on!
target.close()