def bubble(list):
    
    for i in range(0, len(list)-1):
        
        for k in range(0, len(list)-1):
            
            if  list[k]>list[k+1]:
                list[k],list[k+1] = list[k+1],list[k]
    
    return list

print bubble([54,24,23,52,61,21])




