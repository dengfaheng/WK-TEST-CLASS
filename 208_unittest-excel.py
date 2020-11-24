# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 16:32:01 2020
unittest with data in excel 
@author: andrew
"""

import unittest
from moduals.modualstested import *
import pandas as pd

class demoTest(unittest.TestCase):
    """Test five functions"""
    def setUp(self):
        print('\nBefore Testing')
    def tearDown(self):
        print('After Testing')
    
    def test_add(self):
        """Test method add(a, b)"""
        print("Test method add(a, b)")
        for index,row in testdata1.iterrows():
            self.assertEqual(row['sum'], add(row['add1'], row['add2']))
    def test_divide(self):
        """Test method divide(a, b)"""
        print("Test method divide(a, b)")
        for index,row in testdata2.iterrows():
            # print(row['add1'],row['add2'],row['sum'])
            self.assertEqual(row['quotient'], divide(row['dividend'], row['divisor']))
    def test_isEven(self):
        print("Test method isEven(a)")
        self.assertTrue(isEven(4))


if __name__ == '__main__':
    # D:\python\videos\Assignments\PandasVideos
    testdata1 = pd.read_excel(r'.\moduals\testdata.xlsx', sheet_name='Add')
    testdata2 = pd.read_excel(r'.\moduals\testdata.xlsx', sheet_name='Divide')
    unittest.main()


