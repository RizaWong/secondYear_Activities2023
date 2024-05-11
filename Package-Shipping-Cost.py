# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 21:10:50 2023

@author: Rizalyn
"""


weight=eval(input("Weight of the Package: "))

if weight<=5:
    print ("The Shipping Cost: ${weight:.2f}")

elif weight>5:
    print (f"The Shippine Cost: ${weight:.2f}")