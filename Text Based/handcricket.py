import random

#global declarations
global  total_player
global total_comp
total_player = 0 
total_comp=0



#****************************************************************************
#Welcome Function - Prints a welcome message!

print "Welcome to Text Based Hand Cricket - LOL"

#****************************************************************************
#Toss - Decides who bats or bows first

def toss():
    print "Choose Heads or Tails"
    toss_dec = raw_input()
    
    print "\nUser chose %s" %toss_dec
    tossdec_format=toss_dec.lower()
    
    
    if(tossdec_format == "heads" or tossdec_format == "head" or 
       tossdec_format == "tails" or tossdec_format == "tail"):
    
        poss_outcome = ["heads", "tails"]
        result = (random.choice(poss_outcome))  
        print "Toss result was %s" %result
        
        if tossdec_format == result:
            print "\nYou won the toss! Do you want to bat or bowl?"
            user_choice = raw_input()
            if "bat" in user_choice:
                print "You chose to bat first!\n"
                playerfirst_bat()
            else:
                print "You chose to bowl first!\n"
                playerfirst_bowl()
        else:
            print "The computer won the toss"
            x=random.randrange(1,3)
            if x==1:
                print "The computer chose to bat first!\n"
                playerfirst_bowl()
            else:
                print "The computer chose to field first!\n"
                playerfirst_bat()        
    else:
        toss()
   
            

#End of Toss - Somone would've decided something by now
#****************************************************************************



#****************************************************************************
#Batting Mechanics!

def my_choice():
    while True:
        try:
            print "Enter your choice"
            num = int(raw_input())
            break
        except ValueError:
            print "Oops! Enter a number from 1 to 6!"
    if num>6 or num<=0:
        num=6
    return num
    
    
#Computer Choice
def cpu_choice():
    cnum = random.randrange(1, 7)
    return cnum

#End of batting mechanics
#****************************************************************************



#****************************************************************************
#Resets all scores

def new_game():
    print "Let's start a new game!\n"
    global total_player
    global total_comp
    total_player = 0 
    total_comp=0  
    #clear = lambda: os.system('cls')
    #clear()    

#End of function
#****************************************************************************    
       


#****************************************************************************
#If Player chooses to bat first, player innings first  

def playerfirst_bat():
  
    play_num = my_choice()
    print "Player chose %d" %play_num
    comp_num = cpu_choice()
    print "CPU chose %d" %comp_num    
    
    
    
    if play_num != comp_num:
        global total_player
        total_player = total_player+play_num
        print "Your score so far is %d\n" %total_player
        playerfirst_bat()        
        
    else:
        print "Out!"
        print "Your final score is %d" %total_player
        print "CPU needs %d runs to win\n" %(total_player+1)        
        playernext_bowl()   
        print "You're bowling now!\n"

#********End of Player Innings******** 


#********CPU Innings Start********   

def playernext_bowl():  
    
    
    play_num = my_choice()
    print "Player chose %d" %play_num
    comp_num = cpu_choice()
    print "CPU chose %d" %comp_num    
   
   
    if play_num != comp_num:
        global total_comp
        total_comp = total_comp+comp_num
        print "Computer total is %d\n" %total_comp
        if total_comp>total_player:
            print "Computer Wins!\n"
            new_game()
            toss()
        else:   
            playernext_bowl()             
    elif total_comp == total_player and play_num == comp_num:
        print "It's a Tie!!"
        new_game()
        toss()
                   
    else:
        print "Out!"
        print "Computer Total Score was %d" %total_comp
        print "You win by %d runs"%(total_player-total_comp)  
        print "Player Wins!\n"
        new_game()
        toss()

#********End of CPU Innings********   


#End of Match (Player bats first)
#****************************************************************************



#**************************************************************************** 
                              #Useless Code#
    '''if total_comp>total_player:
            print "Computer Wins"
            new_game()      
            
    else:
            print "Player Wins"
            print "Let's start a new game"
            new_game()'''
                            #End of Useless Code#
#**************************************************************************** 



#****************************************************************************
#If player chooses to bowl first, computer bats first

def playerfirst_bowl():
    
    play_num = my_choice()
    print "Player chose %d" %play_num
    comp_num = cpu_choice()
    print "CPU chose %d" %comp_num    
    
   
    
    if play_num != comp_num:
            global total_comp
            total_comp = total_comp+comp_num
            print "CPU total is %d\n" %total_comp
            playerfirst_bowl()
                
    else:
        print "Out!"
        print "CPU final score is %d\n" %total_comp
        print "You need %d runs to win" %total_comp
        playernext_bat() 
        print "You're going to bat now\n"

#********End of Player Innings******** 
        
        
#********CPU Innings Start********         
def playernext_bat():
    
    play_num = my_choice()
    print "Player chose %d" %play_num
    comp_num = cpu_choice()
    print "CPU chose %d" %comp_num    
    
    
        
    if play_num != comp_num:
        global total_player
        total_player = total_player+play_num
        print "Your score is %d\n" %total_player
        if total_player>total_comp:
            print "You Win!\n"
            new_game()
            toss()  
        else:   
            playernext_bat()  
    elif total_player == total_comp and play_num == comp_num:
        print "It's a tie!!" 
        new_game()
        toss()
    else:
        print "Out!"
        print "Your final score is %d\n" %total_player
        print "You lost by %d runs:("%(total_comp-total_player)
        new_game()
        toss()
        

#********End of CPU Innings********  


#End of match (Player bowls first)
#****************************************************************************
        

new_game()
toss()