# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 22:04:40 2023

@author: Rizalyn
"""
score=0
i=0
while i<10:
    from random import randint
    n1=randint (1, 10)
    n2=randint (1, 10)
    
    i=i+1
    ans=int(input("Question " + str(i) + ": " + str(n1) + " x " + str(n2) + " = "))
    
    if ans==n1*n2:
        print ("Right!")
        score=score+1
    else:
        print ("Wrong. The answer is ", n1*n2, ".", sep="")
    
print ("\nTotal Score: ", score, "out of 10.") 
        
        
        