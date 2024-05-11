# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 17:25:32 2023

@author: Rizalyn
"""

import statistics 

num = None
integers=[]
total_sum=0
count=0
index=0

while num!=0:
    count+=1
    num = eval(input("Enter a number (enter 0 to exit): "))
    integers.append(num)
    total_sum+=integers[index]
    index += 1
    
    if num == 0:
        break

mean = statistics.mean(integers)

print (f"\nCOUNT: {count:} \nSUM: {total_sum:.2f} \nMEAN: {mean:.2f}")