#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 17:42:45 2021

@author: raghhav
"""

def convert(list): 
      
    # Converting integer list to string list 
    s = [str(i) for i in list] 
      
    # Join list items using join() 
    res = int("".join(s)) 
      
    return(res) 

def f(a):
    g1 = [int(x) for x in str(a)]
    g1.sort(reverse=True)
    g2 = [int(x) for x in str(a)]
    g2.sort()
    g_1 = convert(g1)
    g_2 = convert(g2)
    f = g_1 - g_2
    return f


n,k = [int(x) for x in input().split()]
first = n
for i in range(k):
    first = f(first)
print(first)