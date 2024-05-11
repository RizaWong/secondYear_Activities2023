# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 20:23:42 2023

@author: Rizalyn

The Fibonacci numbers are the sequence below, where the first two numbers are 1, and 
each number thereafter is the sum of the two preceding numbers. Write a program that
asks the user how many Fibonacci numbers to print and then prints that many. 

1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89
"""

times=eval(input("How many Fibonacci numbers do you want to display? "))

x, y= 1, 1

for i in range (times):
    
    print(x, " ", end="")
    z=x
    x=y
    y=z+x
    

    
