from sys import argv
from os.path import exists

script, from_file, to_file = argv

#print "Copying from %s to %s" %(from_file, to_file)

in_data = open(from_file).read()
#indata = in_file.read()

#print "The input file is %d bytes long" %len(indata)

#print "Does the output file exist? %r" %exists(to_file)
#print "Hit enter when ready"

#raw_input()

out_file = open(to_file, 'w').write(in_data)
#out_file.write(indata)

#print "Alright! All done"

#out_file.close()
#in_file.close()