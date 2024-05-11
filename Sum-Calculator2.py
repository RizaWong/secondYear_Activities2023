# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 18:48:19 2023

@author: Rizalyn
"""

num = None
integers=[]
total_sum=0
count=0
index=0

while num!=0:
    count+=1
    num = eval(input("Enter a number: "))
    integers.append(num)
    total_sum+=integers[index]
    index += 1
    
    if num == 0:
        break

mean = total_sum/(count-1)
print (f"\nCOUNT: {count:} \nSUM: {total_sum:.2f} \nMEAN: {mean:.2f}")