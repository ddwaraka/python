import os
import math


print ("Enter a number")
num = int(raw_input())
intnum = int(math.sqrt(num))
print intnum
print "\n"
num_list=[]
newlist=[]
for i in range (2, num+1):
    num_list.append(i)



print num_list


for k in num_list:
    for j in range (2, 4):
        
        print "K is now %d, j is now %d"%(k,j)
        x=k%j
        if x==0:
            num_list.remove(k)
            print num_list
        
        
            #print "After entering loop x=%d, k=%d, j=%d" %(x,k,j)
        #if x==0:
            #num_list.remove(k)


print "New list = ", newlist
print "Old List", num_list


