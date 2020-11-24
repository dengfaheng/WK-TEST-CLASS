# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 18:03:44 2020
The following functions will be tested by unittest.
@author: kanwa
"""

def add(a, b):
    return a+b

def minus(a, b):
    return a-b

def multi(a, b):
    return a*b

def divide(a, b):
    return a/b

def isEven(a):
    if a % 2 == 0:
        return True
    else:
        return False