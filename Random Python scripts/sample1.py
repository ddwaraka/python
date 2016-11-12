'''import random

#Converts a pre determined string to a number
def name_to_number(name):
    name = name.lower()
    if name=="rock":
        number = 0
    elif name=="spock":
        number = 1
    elif name=="paper":
        number = 2
    elif name=="lizard":
        number=3
    elif name=="scissors":
        number=4
    else:
        print "Invalid Choice"
    
    print "The player chose",name
    return number
    
#Converts a pre determined number to name
def number_to_name(number):
    if number==0:
        name="rock"
    elif number==1:
        name="spock"
    elif number==2:
        name="paper"
    elif number==3:
        name="lizard"
    elif number==4:
        name="scissors"
    else:
        name = "invalid"
        print "Invalid choice"
    
    print "The computer chose",name
    
    return name


#Examines the output of First 2 function and processes it
def rpsls(player_choice):
    p_choice = name_to_number(player_choice)
    comp_number = random.randrange(0,5)
    c_choice = number_to_name(comp_number)
    #print "p_choice ",player_choice
    diff = (p_choice-comp_number)%5
    
    if diff == 0:
        print "There is a tie!\n"
        #print ("                    ")
    if diff  == 1 or diff == 2:
        print "Player Wins!\n"
          #print ("                    ")
    if diff == 3 or diff == 4:
        print "Computer Wins!\n"
         #print ("                    ")   
    new_game()


def new_game():
    print "Enter your choice"
    player_choice = raw_input()
    rpsls(player_choice)    

new_game()'''


print "Enter a number"

num = raw_input()

if num<6:
    print "Success"
else:
    print "No success"

print 6>3
print 3<6