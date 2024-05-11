# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 21:39:49 2023

@author: Rizalyn
"""

num_lists=int(input("How many integers are in the list?"))
integers= []

for i in range (1, num_lists+1): 
    integer=int(input(f'Enter integer {i}:'))
    integers.append(integer)
    
largest=max(integers)
smallest=min(integers)

print (f"The largest number is: {largest}")
print (f"The smallest number is: {smallest}")