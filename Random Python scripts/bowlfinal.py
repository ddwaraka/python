#Bwoling game Kata, developed using Python and Uncle Bob's tutorials


#Sets up the game, initializes an empty array
class Game:
    def __init__(self):
        self.rolls=[]

#Appends every roll to the array above, control then moves on to score()
    def roll(self, pins):
        self.rolls.append(pins)

#Calls respective functions on a case by case basis, all defined at the end of the class
    def score(self):
        result = 0
        
        #Roll Index is roll count (Max = 21)
        rollIndex = 0
        
        #Frame index in the frame count (Max = 10)
        for frameIndex in range(10):
            if self.isstrike(rollIndex):
                result+=self.strikescore(rollIndex)
                rollIndex+=1
            
            elif self.isspare(rollIndex):
                result+=self.sparescore(rollIndex)
                rollIndex+=2
            
            else:
                result+=self.frameScore(rollIndex)
                rollIndex+=2
        print "Total Score: %d\n"%result
        return result


#All Helper functions for strike, spare and score count
    def isspare(self,rollIndex):
        return (self.rolls[rollIndex]+self.rolls[rollIndex+1]==10)
    
    def sparescore(self,rollIndex):
        return self.rolls[rollIndex]+self.rolls[rollIndex+1]+self.rolls[rollIndex+2]
         
    def frameScore(self, rollIndex):
        return self.rolls[rollIndex]+self.rolls[rollIndex+1]  
    
    def isstrike(self,rollIndex):
        return self.rolls[rollIndex]==10
    
    def strikescore(self, rollIndex):
        return 10+self.rolls[rollIndex+1]+self.rolls[rollIndex+2]
    



