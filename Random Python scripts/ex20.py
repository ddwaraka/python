from sys import argv
input_file = raw_input ("Enter the file name: ")

def print_all(f):
    print f.read()

def rewind(f):
    f.seek(0)

def printaline(linecount, f):
   print linecount, f.readline()

current_file = open(input_file)
print "Lets print the whole file:\n"
print_all(current_file)

print "Now, lets rewind like a tape"
rewind(current_file)

print "Lets print 3 lines:"

current_line = 1
printaline(current_line, current_file)

current_line += 1
printaline(current_line, current_file)

current_line += 1
printaline(current_line, current_file)