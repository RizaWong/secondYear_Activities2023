# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 10:41:55 2023

@author: Rizalyn
"""

from random import randint

num = randint(1, 20)
print("This program is a guessing game! \nYou have only 3 chances to play this game.\n")


for i in range(3):
    guess = eval(input("Enter your guess number between 1 and 20: "))
    if guess == num:
        print("Congratulations, you got it!")
        break # walang break sa orig problem 
        
   # elif guess ==2: #2nd way to debug the problem
      #  print("Game over! The correct answer was", num)
        
    else:
        print("Oops, wrong! Please try again.\n")
        
if guess != num: #1st way to debug the problem 
    print("Game over!")