# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 12:25:29 2023

@author: Rizalyn
"""

password="riza1234"

attempts=5
 
while attempts>0:
    attempts-=1
    user = input("Enter Password: ")
    if user!=password and attempts!=0:
        print (f"Incorrect password. You only have now {attempts} more attempts.")
        
    elif user!=password and attempts==0:
        print ("Incorrect password. You've reached the maximum attempts. \nThus, you're kicked off of the system.")
    
    else:
        print ("You are logged in!")
        break
  