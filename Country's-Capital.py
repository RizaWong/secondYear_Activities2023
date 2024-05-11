# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 21:53:34 2023

@author: Rizalyn
"""

name = input ("Enter Name: ")

print ("Hi, " + name + ". Let's have a short quiz.")

print ('Instructions: Write the capital city of the given country.')

c1, c2, c3, c4, c5 = "Manila", "Seoul", "Tokyo", "Jakar", "Hanoi"
score = 0

a1 = input ('1. Capital of Philippines: ')
if a1 == c1:
    score+=1

a2 = input ('2. Capital of Korea: ')
if a2 == c2:
    score+=1

a3 = input ('3. Capital of Japan: ')
if a3 == c3:
    score+=1

a4 = input ('4. Capital of Indonesia: ')
if a4 == c4:
    score+=1

a5 = input ('5. Capital of Vietnam: ')
if a5 == c5:
    score+=1

print (f"Total Score: {score}/5")
