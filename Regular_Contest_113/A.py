#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 17:46:02 2021

@author: raghhav
"""

import math as mt 

MAXN = 200001

# stores smallest prime factor for 
# every number 
spf = [0 for i in range(MAXN)] 

# Calculating SPF (Smallest Prime Factor) 
# for every number till MAXN. 
# Time Complexity : O(nloglogn) 
def sieve(): 
	spf[1] = 1
	for i in range(2, MAXN): 
		
		# marking smallest prime factor 
		# for every number to be itself. 
		spf[i] = i 

	# separately marking spf for 
	# every even number as 2 
	for i in range(4, MAXN, 2): 
		spf[i] = 2

	for i in range(3, mt.ceil(mt.sqrt(MAXN))): 
		
		# checking if i is prime 
		if (spf[i] == i): 
			
			# marking SPF for all numbers 
			# divisible by i 
			for j in range(i * i, MAXN, i): 
				
				# marking spf[j] if it is 
				# not previously marked 
				if (spf[j] == j): 
					spf[j] = i 

# A O(log n) function returning prime 
# factorization by dividing by smallest 
# prime factor at every step 
def getFactorization(x): 
	ret = list() 
	while (x != 1): 
		ret.append(spf[x]) 
		x = x // spf[x] 

	return ret
# precalculating Smallest Prime Factor \
def sol(dic):
    prod = 1
    for n in dic.values():
        prod *= (((n+2)*(n+1))//2)
    return prod
sieve()
x = int(input())
result = 1
for j in range(x,1,-1):
    p = getFactorization(j) 
    d = {}
    for i in p:
        if(i in d):
            d[i] += 1
        else:
            d[i] = 1
    result += sol(d)
print(result)


