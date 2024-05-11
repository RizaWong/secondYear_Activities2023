# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 17:51:13 2023

@author: Rizalyn

One way to find out the last two digits of a number is to mod the number by 100. 
Write a program that asks the user to enter power. Then find the last two digits 
of 2 raised to that power.
"""

power=eval(input("Enter the Exponent for 2: "))
x=2**power
y=x%100

print ("\n2^", power, " = ", x, sep="")
print ("\n", x, "/100 = ",  x/100, sep="")

print ("\nHence, the last two digit of 2 raised to ", power, " is ", y, ".", sep="" ) 