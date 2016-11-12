import textwrap
#Using forloop
def forsort (list):
    for i in range (1, len(list)):
        for j in range (i-1, -1, -1):
            if list[j]>list[j+1]:
                list[j],list[j+1] = list[j+1], list[j]
            
            else:
                break
    return list

print forsort([4,3,1,2])

#hundred = []
#for i in range (100,-1,-1):
    #hundred.append(i)

#print (textwrap.fill('\t'.join(map(str, hundred)).expandtabs(), 80))
#print "\n",(textwrap.fill('\t'.join(map(str, forsort(hundred))).expandtabs(), 80))


#using while loop
def whilesort(list):
    for i in range (0, len(list)):
        j=i-1
        
        while list[j]>list[j+1] and j>=0:
            list[j],list[j+1] = list[j+1],list[j]
            j-=1
    
    return list

print whilesort([4,3,1,2])


#hundred = []
#for i in range (100,-1,-1):
    #hundred.append(i)

#print (textwrap.fill('\t'.join(map(str, hundred)).expandtabs(), 80))
#print "\n",(textwrap.fill('\t'.join(map(str, whilesort(hundred))).expandtabs(), 80))


