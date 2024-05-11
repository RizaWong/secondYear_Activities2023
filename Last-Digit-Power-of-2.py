# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 17:39:33 2023

@author: Rizalyn

(a) One way to find out the last digit of a number is to mod the number by 10.
Write a program that asks the user to enter power. Then find the last digit of 
2 raised to that power.
"""

power=eval(input("Enter the Exponent for 2: "))
x=2**power
y=x%10

print ("\n2^", power, " = ", x, sep="")
print ("\n", x, "/10 = ",  x/10, sep="")

print ("\nHence, the last digit of 2 raised to ", power, " is ", y, ".", sep="" ) 