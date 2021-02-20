#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 17:14:41 2021

@author: raghhav
"""

n = int(input())
if (n % 100 == 0):
    print(100)
else:
    print(100 - (n % 100))