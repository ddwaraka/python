def selsort(list):
    for i in range(0, len(list)):
        min = i
        
        for j in range(i+1, len(list)):
            if list[j]<list[min]:
                min = j
            
        if min!=i:
            list[min],list[i] = list[i],list[min]
        
    return list

print selsort([4,3,2,1])

k=0
while k>=0:
    print "Hi"
    
    
    