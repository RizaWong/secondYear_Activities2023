# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 11:36:55 2023

@author: Rizalyn
"""

hour=eval(input("Enter Hour: "))
day=eval(input("am (1) or pm (2)? "))
future=eval(input("How many hours ahead? "))

new_hour = (hour + future) % 12
 
if new_hour == 0:
    new_hour = 12

if day==1:
    if new_hour==12:
        print (f"\nNew Hour: {new_hour} pm")
    elif new_hour<12:
        print (f"\nNew Hour: {new_hour} am")
    elif new_hour>12:
        print (f"\nNew Hour: {new_hour} am")

else: 
    if new_hour==12:
        print (f"\nNew Hour: {new_hour} am")
    elif new_hour<12:
        print (f"\nNew Hour: {new_hour} pm")
    elif new_hour>12:
        print (f"\nNew Hour: {new_hour} pm")
    