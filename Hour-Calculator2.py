# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 10:19:49 2023

@author: Rizalyn
"""
hour=eval(input("Enter Hour: "))

day=eval(input("am (1) or pm (2)? "))

future=eval(input("How many hours ahead? "))


if (hour+future>24 and day==1):
    print ("\nNew Hour: ", (hour+future)%12, "am")
elif (hour+future>24 and day==2):
    print ("\nNew Hour: ", (hour+future)%12, "pm")
    
elif (hour+future>12 and day==1):
    print ("\nNew Hour: ", hour+future-12, "pm")
elif (hour+future>12 and day==2):
    print ("\nNew Hour: ", hour+future-12, "am")
    
elif (hour+future<12 and day==1):
    print ("\nNew Hour: ", hour+future, "am")
elif (hour+future<12 and day==2):
    print ("\nNew Hour: ", hour+future, "pm")

elif (hour+future==12 and day==2):
    print ("\nNew Hour: ", hour+future, "am")
elif (hour+future==12 and day==1):
    print ("\nNew Hour: ", hour+future, "pm")    