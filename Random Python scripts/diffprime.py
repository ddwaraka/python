import math
import time
import textwrap


def primegen():
    numlist=[]
    notprime = []
    
    while True:
        try:
            print "Enter a number"
            num = int(raw_input())
            
            break
        except ValueError:
            print "\nEnter a number only!\n"
            
    
    start = time.clock()
    
    for number in range (2, num):
        numlist.append(number)
    
    for numb in numlist:
        sqroot = int(math.sqrt(numb))
        #print sqroot
    
        # this inner loop tests numb for primeness
        for x in range (2, sqroot+1):
            if numb % x == 0:
                notprime.append(numb)
                break    # break out of this loop. Control returns to the outer loop.
    
    
    for numbers in notprime:
        numlist.remove(numbers)
    
    
    
    print "\nThere are %d prime numbers between 1 and %d\n" %(len(numlist), num)
    
    
    
    print (textwrap.fill('\t'.join(map(str, numlist)).expandtabs(), 80))
    
    end = time.clock()


    
    print "\nTotal Time = %.2gs\n" % (end-start)
    



primegen()