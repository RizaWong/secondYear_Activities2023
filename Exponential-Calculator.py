# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 23:31:45 2023

@author: Rizalyn
"""

print ("Welcome to the Exponential Calculator!")


i=None 
while i!=0:
    base =eval (input("Enter the base value (or enter 0 to exit):"))
    
    if base==0:
        print ("Thank you for using the Exponential Calculator. ")
        break
    
    else:
        exponent=eval (input("Enter the exponent value: "))
        answer=base**exponent
        print (f"The answer is: {answer}")