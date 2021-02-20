#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 17:32:34 2021

@author: raghhav
"""

s = input()
odd = list(range(0,len(s),2))
even = list(range(1,len(s),2))
odds = ""
evens = ""
for i in odd:
    odds += s[i]
for j in even:
    evens += s[j]
val1 = odds.islower()
val2 = evens.isupper()
if (evens == ""):
    fin = val1
elif(odds == ""):
    fin = val2
else:
    fin = val1 and val2
if (fin == True):
    print("Yes")
else:
    print("No")