# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 20:23:54 2023

@author: Rizalyn

Write a program that asks the user to enter power and how many digits they want. 
Find the last that many digits of 2 raised to the power the user entered.
"""

power=eval(input("Enter the Exponent for 2: "))
digit=eval(input("Number of Last Digit: "))
x=2**power

print ("\n2^", power, " = ", x, sep="")

y=x%(10**digit)

print ("\n", x, "/", (10**digit), " = ",  x/(10**digit), sep="")
print ("\nLast", digit, " Digits: ", y)

