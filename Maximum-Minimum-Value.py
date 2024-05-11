# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 17:00:51 2023

@author: Rizalyn
"""

largest=0
smallest=0
num=""
integers =[]

while num != 0:
    num = int(input("Type an integer: "))
    
    if num>largest:
          largest = num
    elif num == 0:
        smallest=smallest
        break
    elif num<largest:
        smallest = num
    integers.append(num)
        
difference = max(integers)-min(integers)
print(" the largest number is ", max(integers), "and the smallest number is", min(integers))
print(f"The difference of the two numbers is {difference}")