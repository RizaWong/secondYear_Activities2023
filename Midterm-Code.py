# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 15:03:15 2023

@author: Rizalyn
"""
i = 0

while i<2: 
    
    print ("\n\nEnter two numbers and an operator to perform calculation (or any symbol to exit): ")
    
    num1 = eval (input ("Enter the first number: "))
    
    num2 = eval (input ("Enter the second number: "))
    
    operation = input('Enter Operator { +, -, *, **, / } ') 

    if operation == "+":
        print (f"{num1:.1f} + {num2:.1f} = {num1+num2:.1f}")

    elif operation == "-":
        print (f"{num1:.1f} - {num2:.1f} = {num1-num2:.1f}")

    elif operation == "*":
        print (f"{num1:.1f} * {num2:.1f} = {num1*num2:.1f}")

    elif operation == "**":
        print (f"{num1:.1f} ** {num2:.1f} = {num1**num2:.1f}")

    elif operation == "/":
        print (f"{num1:.1f} / {num2:.1f} = {num1/num2:.1f}")
    
    else: 
        print ("\nExiting Calculator...")
        break
    
print ("Thank you for using the calculator!")
