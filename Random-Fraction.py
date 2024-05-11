# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 17:30:15 2023

@author: Rizalyn
"""
import random

num_problems = int(input("How many problems do you want to generate? "))
correct_answers = 0

for i in range(num_problems):
    # Generate two random fractions
    numerator1 = random.randint(1, 10)
    denominator1 = random.randint(numerator1, 10)
    fraction1 = f"{numerator1}/{denominator1}"
    
    numerator2 = random.randint(1, 10)
    denominator2 = random.randint(numerator2, 10)
    fraction2 = f"{numerator2}/{denominator2}"
    
    # Multiply the fractions and ask the user for the answer
    answer = numerator1 * numerator2
    expected_denominator = denominator1 * denominator2
    user_answer = input(f"What is {fraction1} * {fraction2}? ")
    
    # Check if the user's answer is correct
    if user_answer == str(answer) + '/' + str(expected_denominator):
        print("Correct!")
        correct_answers += 1
    else:
        print("Incorrect.")
    
# Calculate and print the score
score = correct_answers / num_problems * 100
print(f"You got {correct_answers} out of {num_problems} problems correct. ({score:.1f}% score)")

