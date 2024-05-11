# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 19:57:22 2023

@author: Rizalyn

Write a program that asks the user for their name and how many times to print it. 
The program should print out the user's name the specified number of times.
"""

name=str(input("What is your name? "))

times=eval(input("How many times do you want to repeat your name? "))

print ("\n")

for i in range (times):
    print (name)