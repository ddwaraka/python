from sys import argv
script, fname = argv

target = open(fname, 'r')

print target.read()

