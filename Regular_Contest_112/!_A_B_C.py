#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 12:26:16 2021

@author: raghhav
"""
 
def solve():
	l,r=[int(x) for x in input().split()]
	n=r-l*2
	if n<0:
		print(0)
		return
	print((n+1)*(n+2)//2)
	
 
t=int(input())
for _ in range(t):
	solve()