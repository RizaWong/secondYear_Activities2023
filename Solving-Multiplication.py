# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 00:31:12 2023

@author: Rizalyn
"""

import random

score= 0

num_problem = eval (input ('How many problems to generate? '))

for i in range (num_problem):

    num1 = random.randint (1, 10)
    num2 = random.randint (1, 10)
    

    
    question = eval (input (f'{i+1}.) {num1} x {num2} = '))
    answer = num1*num2
    
    if question == answer:
        score+=1

print (f"Total Scores: {score}")
    
    
    



