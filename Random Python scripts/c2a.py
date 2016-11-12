import random

#Converts a pre determined string to a number
def name_to_number(name):
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
    
    
    return number
    
#Converts a pre determined number to name
def number_to_name(number):
    if number==0:
        name="Rock"
    elif number==1:
        name="Spock"
    elif number==2:
        name="Paper"
    elif number==3:
        name="Lizard"
    elif number==4:
        name="Scissors"
    else:
        name = "invalid"
        print "Invalid choice"
    
    print "The computer chose",name
    
    return name


#Examines the output of First 2 functions and processes it
def rpsls(player_choice):
    p_choice = name_to_number(player_choice)
    comp_number = random.randrange(0,5)
    c_choice = number_to_name(comp_number)
    #print "p_choice ",player_choice
    diff = (p_choice-comp_number)%5
    
    if diff == 0:
        print "There is a tie!\n"
        #print ("                    ")
        playerentry()
    if diff  == 1 or diff == 2:
        print "Player Wins!\n"
          #print ("                    ")
        playerentry()
    if diff == 3 or diff == 4:
        print "Computer Wins!\n"
         #print ("                    ")     
        playerentry()
    '''else:
         print "No Result"'''

def playerentry():
    
        print "Enter your choice"
        entry = raw_input()
        print "You chose %s" %entry
        entry=entry.lower()
        list = ['rock', 'paper', 'scissors', 'lizard', 'spock']
        if entry in list:
            rpsls(entry)
        else:
            print "Oops! Choose between Rock, Paper, Scissors, Lizard or Spock!"
            playerentry()

playerentry()

