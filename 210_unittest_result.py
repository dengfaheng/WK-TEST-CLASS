# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 10:25:50 2020
To output result of unittest 
@author: andrew
"""


import unittest
from moduals.modualstested import *


class demoTest(unittest.TestCase):
    """Test five functions"""
    @classmethod
    def setUpClass(cls):
        print('\nBefore all Testing')
    @classmethod
    def tearDownClass(cls):
        print('After all Testing')
    def setUp(self):
        print('\nBefore Testing')
    def tearDown(self):
        print('After Testing')

    def test_add(self):
        """Test method add(a, b)"""
        print("\nTest method add(a, b)")
        self.assertEqual(5.0, add(3, 2))
    def test_minus(self):
        """Test method minus(a, b)"""
        print("Test method minus(a, b)")
        self.assertEqual(1, minus(3, 2))
    def test_multi(self):
        """Test method multi(a, b)"""
        print("Test method multi(a, b)")
        self.assertEqual(6, multi(2, 3))
    def test_divide(self):
        """Test method divide(a, b)"""
        print("Test method divide(a, b)")
        self.assertEqual(2.1, divide(6, 3))
    @unittest.skip("demonstrating skipping ")
    def test_isEven(self):
        print("Test method isEven(a)")
        self.assertTrue(isEven(4))
if __name__ == '__main__':
    suite = unittest.TestSuite()
    tests = [demoTest("test_add"),demoTest("test_minus"),demoTest("test_multi"),
             demoTest("test_isEven"),demoTest("test_divide")]
    suite.addTests(tests)
    runner = unittest.TextTestRunner(verbosity=2)
    test_results = runner.run(suite)
    print("*********Summary*******************1")
    print(test_results.wasSuccessful())
    print(test_results.testsRun)
    print(len(test_results.failures))
    print(len(test_results.skipped))
    print("*********Failures******************2")
    for case, reason in test_results.failures:
        print(case.id())
        print(reason)
    print("**********Skipped *****************3")
    for case, cause in test_results.skipped:
        print(case.id())
        print(cause)
