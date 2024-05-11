# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 21:00:09 2023

@author: Rizalyn
"""

num_lists=int(input("How many integers are in the list?"))
total=0

for i in range (1, num_lists+1): 
    integer=eval(input(f'Enter integer {i}:'))
    total+=integer
    
average=total/(num_lists)

print (f'The average of the list is: {average:.2f}')