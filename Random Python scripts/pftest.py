import pf
from pf import factor 


import unittest

class pftest(unittest.TestCase):
    
    def test_for_lowest_non_prime(self):
        self.assertEquals([2,2], factor(4))
        
    def test_for_primes(self):
        self.assertEquals([1,2], factor(2))
        self.assertEquals([1,3], factor(3))
        self.assertEquals([1,5], factor(5))
    
    def test_for_diverse_primes(self):
        self.assertEquals([2,3,5,7], factor(210))
        self.assertEquals([3,5,7], factor(105))
    
    def test_check_for_multiple_repeating_primes(self):
        self.assertEquals([2,2,2,2], factor(16))
        self.assertEquals([3,3,3,3], factor(81))
    
    


if __name__=="__main__":
    unittest.main()