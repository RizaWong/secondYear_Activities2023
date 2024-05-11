# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 12:28:09 2023

@author: Rizalyn
"""

from random import randint 

num=randint (1, 20)
print("This program is a guessing game! \nYou have only 3 chances to play this game.\n")



while True:
    
    for i in range(3):

        guess=eval(input("Type your guess number between 1 and 20: "))
        if guess==num:
            print ("CONGRATULATIONS, you got it!")
            break 

        elif i==1:
            print ("Oops, wrong! You now only have one more attempt.")
        
        elif i==2:
            print("Oops, wrong! GAME OVER.\nThe correct answer is ", num, ".", sep="")
        
        else: 
            print ("Oops, wrong! Please try again.")
    
    

    repeat=input ("Enter 'YES' to try again and 'NO' to end the game: ")
    
    if repeat=="NO" or "no":
        print ("Thank you for participating with us!")
        break

    
    
