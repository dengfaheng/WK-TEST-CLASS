# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 19:10:41 2020
unittest 
@author: andrew
"""

import unittest


# 被测函数
def add(a, b):
    return a + b


def minus(a, b):
    return a - b


def multi(a, b):
    return a * b


def divide(a, b):
    return a / b


# 测试用例
class DemoTest(unittest.TestCase):
    """Test four functions"""

    def test_add(self):
        """Test method add(a, b)"""
        print("\nTest method add(a, b)")
        # self.assertEqual(4, add(2, 2))
        self.assertEqual(4.2E100, add(2.1E100, 2.1E100))

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
        self.assertEqual(2, divide(6, 3))

    def test_split(self):
        print("Test string method split(a, b)")
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])

    def test_isupper(self):
        print("Test isupper1")
        self.assertTrue('FOOa'.isupper())
        print("Test isupper2")
        self.assertFalse('Fo'.isupper())


if __name__ == '__main__':
    unittest.main()
