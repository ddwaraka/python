# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions
import random
def name_to_number(name):
    # delete the following pass statement and fill in your code below
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
    # convert name to number using if/elif/else
    # don't forget to return the result!


def number_to_name(number):
    # delete the following pass statement and fill in your code below
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
        print "Invalid choice"
    return name
    print "The computer chose ",name

# convert number to a name using if/elif/else
# don't forget to return the result!
    
print """Enter your choice: 
    Rock, Spock, Paper, Lizard, Scissors"""
player_choice=raw_input()
print "Player chose ",player_choice
#print "                                      "
p_choice = name_to_number(player_choice) 
def rpsls(player_choice): 
    '''# delete the following pass statement and fill in your code below
    print """Enter your choice: 
    Rock, Spock, Paper, Lizard, Scissors"""
    player_choice=raw_input()
    print "Player chose ",player_choice
    print "                                      "
p_choice = name_to_number(player_choice) '''
# print a blank line to separate consecutive games

# print out the message for the player's choice
#print "Player chose ",player_choice

# convert the player's choice to player_number using the function name_to_number()
#p_choice = name_to_number(player_choice)   
# compute random guess for comp_number using random.randrange()
comp_number = random.randrange(0,5)
# convert comp_number to comp_choice using the function number_to_name()
c_choice = number_to_name(comp_number)
# print out the message for computer's choice
#print "The computer chose ",name
# compute difference of comp_number and player_number modulo five
if p_choice-c_choice==1 or 2:
    print "Player Wins"
if p_choice-c_choice==3 or 4:
    print "Computer Wins"
# use if/elif/else to determine winner, print winner message

    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


