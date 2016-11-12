a = [5,4,3,2,1]

print sorted(a, reverse=True)


#For example, if list[2] contains a value that is even, that value should 
#be included in the new list, since it is also at an even index (i.e., 2) 
#in the original list. However, if list[3] contains an even number, that 
#number should not be included in the new list since it is at an odd index (i.e., 3) 
#in the original list.

n = [1,2,4,5,7,9,11]

new_n = []
print len(n)


for i in range (1, len(n), 2):
    print n[i]



for i in range (1, len(n), 2):
    if n[i]%2==0:
        new_n.append(n[i])

print new_n


