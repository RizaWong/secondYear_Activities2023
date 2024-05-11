# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 18:09:52 2023

@author: Rizalyn
"""
import random

score = 0

num_problem = eval (input('How many problems do you want?'))

for i in range (num_problem):
    
    operation = input('What operation do you want? { +, -, x, / } ') 
   
    num1 = random.randint (1, 10)
    num2 = random.randint (1, 10)
    
    if operation == "+":
        problem = eval (input(f"What is {num1} + {num2} = "))
        if problem == num1+num2:
            print('Correct.')
            score+=1
        else:
            print('Incorrect. Answer: ', num1+num2)
    elif operation == "-":
        problem = eval (input(f"What is {num1} - {num2} = "))
        if problem == num1-num2:
            print('Correct.')
            score+=1
        else:
            print('Incorrect. Answer: ', num1-num2)
    elif operation == "x":
        problem = eval (input(f"What is {num1} x {num2} = "))
        if problem == num1*num2:
            print('Correct.')
            score+=1
        else:
            print('Incorrect. Answer: ', num1*num2)
    elif operation == "/":
        problem = eval (input(f"What is {num1} / {num2} = "))
        if problem == num1/num2:
            print('Correct.')
            score+=1
        else:
            print('Incorrect. Answer: ', num1/num2)

print (f'Score: {score}/{num_problem}')

    
   
    