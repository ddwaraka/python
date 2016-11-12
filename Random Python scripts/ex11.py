#print "How old are you?",
#age = int(raw_input())
print "How tall are you?",
height = float(raw_input())
#print "How much do you weigh?",
#weight = float(raw_input())

#print "So, you're %s years old, %r ft tall and weigh %s kgs"%(
    #age, height, weight)

ft, inches = divmod (height, 1)
print inches
inch = str (inches)
print len(inch)
if (len(inch)<=3):
   inches = inches*10
else:
   inches = inches*100
print "%d Ft and %d inches" %(ft, inches)


'''if (inch==10.0 or inch==20.0): #or inch==30.0 or inch==40.0 or inch==50.0 or inch==60.0 or inch==70.0 or inch==80.0 or inch==90.0):
    inch = inch/10
    print inch
else:
   inch = inch*100'''
#print inch
'''s=1234.5678
i, d = divmod (s, 1)
print i
print d
print 0.2*10'''

