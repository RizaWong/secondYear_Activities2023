# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 18:48:09 2023

@author: Rizalyn
"""

meal_cost = eval(input("Enter the cost of the meal: "))
tax_percentage = eval(input("Enter the percentage of tax to be added (e.g., 8 for 8%): "))
tip_percentage = eval(input("Enter the percentage of tip to be added (e.g., 15 for 15%): "))

tax = meal_cost * (tax_percentage / 100)
tip = meal_cost * (tip_percentage / 100)
total_cost = meal_cost + tax + tip

print (f'Tax: {tax} \nTip: {tip}')

print(f"The total cost of the meal is {total_cost:.2f}")
