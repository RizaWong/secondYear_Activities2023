# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 10:12:52 2023

@author: Rizalyn
"""

price=float(input("Enter the Price of the Meal: ₱"))
tip=int(input("Enter the Tip Percentage(%): "))
tip_amount=((price/100)*tip)
total_bill=(price+tip_amount)
print ("\nTIP AMOUNT: ₱",tip_amount, "\nTOTAL BILL: ₱",total_bill)
