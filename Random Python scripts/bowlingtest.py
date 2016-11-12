import bowlfinal
from bowlfinal import Game
import unittest

class Bowlingtest(unittest.TestCase):
    def setUp(self):
        self.game=Game()
    
    def test_guttertest(self):
        self.rollmany(0,20)
        self.assertEquals(0, self.game.score())
       
    
    def test_onlyones(self):    
        self.rollmany(1,20)
        self.assertEquals(20, self.game.score())
    
    def test_onespare(self):
        self.game.roll(5)
        self.game.roll(5)
        self.game.roll(3)
        self.rollmany(0,17)
        self.assertEquals(16,self.game.score())
    
    def test_onestrike(self):
        self.game.roll(10)
        self.game.roll(4)
        self.game.roll(3)
        self.rollmany(0,16)
        self.assertEquals(24, self.game.score())
    
    def test_allstrikes(self):
        self.rollmany(10,12)
        self.assertEquals(300, self.game.score())
    
    def test_allspares(self):
        for i in range(20):
            self.rollspares()
        self.assertEquals(150, self.game.score())
    
    def test_allzeros(self):
        self.rollmany(0,20)
        self.assertEquals(0, self.game.score())
    
    def test_gutterspares(self):
        for i in range(20):
            self.game.roll(0)
            self.game.roll(10)
        self.assertEquals(100, self.game.score())
    
    def test_oneEntiregame(self):
        self.game.roll(3)
        self.game.roll(4)
        self.game.roll(5)
        self.game.roll(5)
        self.game.roll(3)
        self.game.roll(2)
        self.game.roll(10)
        self.game.roll(9)
        self.game.roll(0)
        self.game.roll(5)
        self.game.roll(4)
        self.game.roll(4)
        self.game.roll(6)
        self.game.roll(9)
        self.game.roll(0)
        self.game.roll(8)
        self.game.roll(1)
        self.game.roll(5)
        self.game.roll(5)
        self.game.roll(4)        
        self.assertEquals(113, self.game.score())
        
    def test_get200(self):
        self.rollstrike()
        self.rollspares()
        self.rollstrike()
        self.rollspares()    
        self.rollstrike()
        self.rollspares()
        self.rollstrike()
        self.rollspares()    
        self.rollstrike()
        self.rollspares()
        self.rollstrike()
        self.assertEquals(200, self.game.score())
        
    def rollmany(self,pins,rolls):
        for i in range(rolls):
            self.game.roll(pins)
    
    def rollspares(self):
        self.game.roll(5)
        self.game.roll(5)
    
    def rollstrike(self):
        self.game.roll(10)
        
    


if __name__=="__main__":
    unittest.main()        