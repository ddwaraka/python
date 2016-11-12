def add (a,b):
    print "Adding %d and %d" %(a,b)
    return a+b

def sub (a,b):
    print "Subtracting %d and %d" %(a,b)
    return a-b

def mul (a,b):
    print "Multiplying %d and %d" %(a,b)
    return a*b

def div(a,b):
    print "Dividing %d and %d" %(a,b)
    return a/b

age = add (30,5)
height = sub (40,20)
weight = mul(90,2)
iq = div (380,2)

print "Age is %d" %age
#print "Cars = %d" %cars

print "Here's a nice puzzle to solve"
what = add(age, sub(height, mul(weight, div(iq, 2))))   
print what 