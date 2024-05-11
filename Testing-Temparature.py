# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 20:13:07 2023

@author: Rizalyn
"""

def check_temp(temp):
    if  temp < 15:
        print('Bring a jacket')
    elif temp > 15 and temp < 35:
        print('Pack a jacket')
    elif temp > 35:
        print('Leave the jacket at home')
        
check_temp (17)
check_temp (37)
check_temp (14)