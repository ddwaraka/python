import learntest
from learntest import mycontains, myfirst
import unittest

class TestMyFunctions(unittest.TestCase):
    def test_contains_simple_true(self):
        self.assertTrue(mycontains(3,[1,2,3]))
    
    def test_my_first(self):
        self.assertEqual(myfirst([1,3,5]), 1)
    
        def test_first_empty(self):
            self.assertRaises(IndexError, myfirst, [])    
        

if __name__=="__main__":
    unittest.main()