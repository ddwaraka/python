import math


def primecheck(number):
    numsq = int(math.sqrt(number))
    
    #if number == 2 or number==3:
        #print "Prime2or3!",number
    
    for i in range (2, numsq+1):
        if number%i == 0:
            print "Not Prime!",number
            break
    else:
        print "Prime!",number



primecheck(3)

i=0
for i in range(0, 10):
    pass

x=i

print x
