# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 11:08:50 2020

D:\python\videos\Assignments\PandasVideos
D:\python\videos\Assignments\PandasVideos\moduals
testfixture  setup teardown
@author: kanwa
"""
import unittest
from moduals.modualstested import *

class demoTest(unittest.TestCase):
    """Test five functions"""
    def setUp(self):
        print('\nBefore Testing')
    def tearDown(self):
        print('After Testing')
    
    def test_add(self):
        """Test method add(a, b)"""
        print("Test method add(a, b)")
        self.assertEqual(4.2E100, add(2.1E100, 2.1E100))
    def test_divide(self):
        """Test method divide(a, b)"""
        print("Test method divide(a, b)")
        self.assertEqual(2, divide(6, 3))
    def test_isEven(self):
        print("Test method isEven(a)")
        self.assertTrue(isEven(4))

from moduals import modualstested
class demoTest2(unittest.TestCase):
    """Test five functions"""
    def setUp(self):
        print('\nBefore Testing')
    def tearDown(self):
        print('After Testing')
    
    def test_add(self):
        """Test method add(a, b)"""
        print("Test method add(a, b)")
        self.assertEqual(4.2E100, modualstested.add(2.1E100, 2.1E100))
    def test_divide(self):
        """Test method divide(a, b)"""
        print("Test method divide(a, b)")
        self.assertEqual(23, modualstested.divide(6, 3))
    def test_isEven(self):
        print("Test method isEven(a)")
        self.assertTrue(modualstested.isEven(4))
        
        
if __name__ == '__main__':
    unittest.main()