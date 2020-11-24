# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 17:12:39 2020

@author: 12615
"""
import sys
import unittest
import HTMLTestRunner


class testadd(unittest.TestCase):
    def setUp(self):
        pass

    def test_add1(self):
        self.assertEqual(2 + 3 + 10, 15)

    def test_add2(self):
        self.assertEqual(10 + 150, 160)

    def test_add3(self):
        # 一处出错，查看测试结果
        self.assertEqual(2 * 5 * 7, 70)

    def tearDown(self):
        pass


def suite():
    suiteTest = unittest.TestSuite()
    suiteTest.addTest(testadd("test_add1"))
    suiteTest.addTest(testadd("test_add2"))
    suiteTest.addTest(testadd("test_add3"))
    return suiteTest


if __name__ == "__main__":
    # 存放路径在E盘目录下
    filepath = 'myreports/py_result.html'
    fp = open(filepath, 'wb')
    # 定义测试报告的标题与描述
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'测试报告标题', description=u'测试报告描述')
    runner.run(suite())
    fp.close()
