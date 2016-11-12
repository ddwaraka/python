global player_score
player_score = 0
global comp_score
comp_score = 0

def score(player, comp):
    global player_score
    global comp_score
   
    player_score+=player
    comp_score+=comp    
    
    if player_score<40 and comp_score<40:
        
        
        
        if player_score==40 and comp_score<40:
            print "Player Wins"
        
        elif comp_score==40 and player_score<40:
            print "Comp Wins"
        
    else:
        print "Deuce"
        
    


    
    




score(15,15)
score(15,15)
score(10,10)
score(10,0)

print player_score
print comp_score