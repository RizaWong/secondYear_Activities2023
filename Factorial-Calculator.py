# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 19:34:50 2023

@author: Rizalyn
"""

#import math (shortcut for factorial)
#factorial = math.factorial (num)


#manually getting the factorial of number

factorial = 1
while True: 
    num = int (input('Please enter a positive number: '))
    
    if num < 0:
        print ("Sorry, factorial does not exist for negative numbers. ")
        break
    
    elif num == 0:
        print ("Factorial Value: 1")
    
    else:
        for i in range (1, num+1):
            factorial = factorial * i
        print (f"Factorial Value: {factorial}")