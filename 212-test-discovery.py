# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 18:34:51 2020
Test discovery 探索性测试
三段代码 分别运行 不要一次运行
@author: andrew
"""

import unittest

# 第一段代码 定义测试目录
# test_dir = r'./subtests'
# discover = unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')
# runner = unittest.TextTestRunner()
# runner.run(discover)

# 第二段代码 利用suite 匹配测试模块名字
# test_dir = r'./subtests'
# suite = unittest.TestSuite()
# all_cases = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')
# [suite.addTests(case) for case in all_cases]
# # for case in all_cases:
# #     suite.addTests(case)
# unittest.TextTestRunner().run(suite)

# 第三段代码 #将测试模块一一添加
import pandas as pd
path = './subtests/discovercase.xlsx'
df = pd.read_excel(path,sheet_name='Sheet1')
suite = unittest.TestSuite()
for index, row in df.iterrows():
    # print(case)
    discover = unittest.defaultTestLoader.discover(row['Path'], pattern=row['filename'])
    print(discover)
    suite.addTest(discover)

# unittest.TextTestRunner().run(suite)
