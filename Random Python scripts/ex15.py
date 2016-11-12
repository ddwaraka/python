from sys import argv
script, sample = argv

sampleT = open(sample)


print sampleT.read()

sampleT.close()
sampleT.truncate()

sampleT.write("Hello")

sampleT = open(sample)
print sampleT.read()
#sample.close()
#print "File closed"

#sampleT2 = open(sample)

