import unittest

import fb

from fb import fizzbuzz

class fbtest(unittest.TestCase):
    
    def test_fizz(self):
        self.assertEquals("Fizz", fizzbuzz(3))
    
    def test_buzz(self):
        self.assertEquals("Buzz",fizzbuzz(5))
    
    def test_fizzbuzz(self):
        self.assertEquals("FizzBuzz",fizzbuzz(15))
    
    def test_neither(self):
        self.assertEquals(2, fizzbuzz(2))



if __name__=="__main__":
    unittest.main()