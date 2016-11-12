from sys import argv
script, uname, lname = argv
prompt = '>>'

print "Hi! %s %s, this is %s" %(uname, lname, script)
print "Are you guy or a girl?"
gen = raw_input()
if (gen=='guy' or gen=='Guy' or gen=='Male' or gen=='male'):
    pref = "Mr"
elif:
    pref = "Ms"
print "I will now call you %s %s" %(pref, lname)
print "I'd like to ask you a few questions"
print "Do you like me %s %s?" %(pref, lname)
likes = raw_input(prompt)

print "Where do you live %s %s?" %(pref, lname)
lives = raw_input(prompt)

print "What kind of computer do you have?"
comp = raw_input(prompt)

print """
Alright %s %s! So you said %s about liking me. 
You live in %s and
You have a %s computer """ %(pref, lname, likes, lives, comp)