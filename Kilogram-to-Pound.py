# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 10:30:15 2023

@author: Rizalyn
"""

while True:
    weight_kg = eval(input("Enter a weight in kilograms: "))
    if weight_kg < 0:
        print("Invalid entry. Weight must be non-negative.")
        continue #if the input of the user is negative(True within this statement) it'll repeat this code 
        #of block then ask the user enter another input. But if it false, it'll execute the 
        #remaining code of block
    else:
        break

weight_lb = weight_kg * 2.20462
print("Weight in pounds: ", round(weight_lb, 1))
