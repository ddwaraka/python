def quicksort(list):
    left = []
    right = []
    if len(list)>1:
        pivot = (len(list))/2
        print "len = ", len(list)
        print "pivot index = ", pivot
        print "pivot value = ", list[pivot]
        print "list before sorting = ", list
        for i in range(0, len(list)):
            if list[i]>list[pivot]:
                right.append(list[i])
            
            else:
                left.append(list[i])
                
        return quicksort(left)+quicksort(right)
    else:
        return list


print quicksort([4,3,2,1])
