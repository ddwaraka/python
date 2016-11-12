print "Enter the number of people"
people = int(raw_input())

print "Enter the number of cats"
cats = int(raw_input())

print "Enter the number of dogs"
dogs = int(raw_input())

print """So you said there are:
%d People
%d Cats
%d Dogs"""%(people,cats,dogs)



if people < cats:
    print "Too many cats, the world is doomed!"

if people > cats:
    print "Not many cats, the world is saved!"
    
elif people == cats:
    print "Shit! God save us now!"
 
if people < dogs:
    print "The world is drooled on!"
    
if people > dogs:
    print "The world is dry!"
    

#dogs+=5

if people >= dogs:
    print "People are greater than or equal to dogs"

elif people<= dogs:
    print "People are less than or equal to dogs"

else:
    print "People are dogs" 