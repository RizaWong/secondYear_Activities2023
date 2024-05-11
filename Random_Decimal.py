# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 16:55:57 2023

@author: Rizalyn

Write a program that generates a 5 random decimal number between 1 and 100 with 
two decimal places of accuracy. Examples are 1.23, 3.45, 9.80, and 5.00. Compute 
the average of the numbers. 

"""

from random import uniform 

a=(round(uniform(1,100), 2))

b=(round(uniform(1,100), 2))

c=(round(uniform(1,100), 2))

d=(round(uniform(1,100), 2))

e=(round(uniform(1,100), 2))

print ("Five Random Numbers: ", a, ", ", b,", ", c, ", ", d, ", and ", e, ".", sep="") 

ave=(a+b+c+d+e)/5

print ("\nAverage: ", round (ave,2), ".", sep="")