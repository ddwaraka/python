def ch_cr (chcount, crcount):
    print "You have %d Cheese" %chcount
    print "You have %d Crackers" %crcount
    #print "That's enough for a party"
    #print "Get a blanket!!"

print "We could give numbers directly"
ch_cr(50, 20)
raw_input("Press Enter to move onto next part")


print "Or we could use variables"
chcount = 30
crcount = 40
ch_cr (chcount,  crcount)
raw_input("Press Enter to move onto next part")

print "We can also do math in it"
ch_cr(50+10, 60+40)
raw_input("Press Enter to move onto next part")


print "And we can also do math with variables"
ch_cr(chcount+100, crcount+40)

print "Or we could take input from the user directly"
chcount = int(raw_input("Enter the number of Cheese boxes you have: "))
crcount = int(raw_input("Enter the number of Cracker boxes you have: "))
ch_cr(chcount, crcount)

