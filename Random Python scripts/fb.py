def fizzbuzz(i):
    if i%5==0 and i%3==0:
        print "FizzBuzz"
        return "FizzBuzz"
    
    elif i%3==0:
        print "Fizz"
        return "Fizz"
        
    elif i%5==0:
        print "Buzz"
        return "Buzz"
    
    else:
        print i
        return i


for i in range (1, 101):
    fizzbuzz(i)