# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 10:25:50 2020
Get yourself results
@author: andrew
"""


import unittest
from moduals.modualstested import *
import matplotlib.pyplot as plt
import pandas as pd

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
    tests = [demoTest("test_add"),demoTest("test_minus"),demoTest("test_multi"),demoTest("test_isEven"),demoTest("test_divide")]
    suite.addTests(tests)
    runner = unittest.TextTestRunner(verbosity=2)
    test_results = runner.run(suite)
    print("***************************1")
    print(test_results.wasSuccessful())
    print(test_results.testsRun)
    print(len(test_results.failures))
    print(test_results.failures)
    print("***************************2")
    for case , reason in test_results.failures:
        print(case.id())
        print(reason)
    for case , cause in test_results.skipped:
        print(case.id())
        print(cause)
        
        
    
    # excel
    path = r'.\myreports\myreport.xlsx'
    writer = pd.ExcelWriter(path, engine = 'openpyxl')
    
    
    labels = 'Passes', 'Failures', 'Skippings'
    passes = test_results.testsRun - len(test_results.failures) - len(test_results.skipped)
    failures = len(test_results.failures)
    skippings = len(test_results.skipped)
    df = pd.DataFrame(columns=['Pass', 'Failures', 'Skipped'])
    new_row = {'Pass':passes, 'Failures':failures, 'Skipped':skippings}
    df = df.append(new_row, ignore_index=True)
    df.to_excel(writer,sheet_name='summary')
    df = pd.DataFrame(columns=['FailuresName', 'Failuresreason'])
    for case , reason in test_results.failures:
        new_row = {'FailuresName':case.id(), 'Failuresreason':reason}
        df = df.append(new_row, ignore_index=True)
    df.to_excel(writer,sheet_name='failures')    
    df = pd.DataFrame(columns=['SkippedName','SkippedCause'])
    for case , cause in test_results.skipped:
        new_row = {'SkippedName':case.id(), 'SkippedCause':cause}
        df = df.append(new_row, ignore_index=True)
    df.to_excel(writer,sheet_name='skipped')  
    writer.save()
    writer.close()
    
    # image
    sizes = [passes, failures, skippings]
    explode = (0.1, 0.0 , 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.show()
