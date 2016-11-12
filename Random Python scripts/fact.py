def factorial (n):
    fact = 1
    
    while n>0:
        fact*=n
        
        n-=1
    return fact

print factorial(4)


def recurfact(n):
    if  n==0:
        return 1
    
    else:
        return n*recurfact(n-1)

print recurfact(4)

n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
# Add your function here



def flatten(lists):
    results = []
    
    results = lists[0]+lists[1]
    
    return results


        



print flatten(n)
print n[0]+n[1]

