# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 20:11:19 2023

@author: Rizalyn
"""

import random

numbers = [ 1, 2, 3, 4, 5]

random.shuffle(numbers)

print (numbers)

number = random.choice(numbers)
print(number)