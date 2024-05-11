# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 15:12:52 2023

@author: Rizalyn
"""
A1, A2, A3, A4 = "Macchiato", "Capuccino", "Iced Coffee", "Hot Choco"
P1, P2, P3, P4 = "P 105", "P 95", "P 75", "P 65"
p1, p2, p3, p4= 0, 0, 0, 0

print ("\t\t\t\t\t\t\t\t\t\t\tRiza's Cafe")
print ("\n\t\t\t\t\t\t\t\t\t\t\t\tMENU")
print ("\n\n \t\t\t\t\t\t----------------------------------------------------\n\n")

print ("\t\t\t\t\t\t\t\tCode\t\tDescription\t\t\tPrice")
print ("\t\t\t\t\t\t\t\tA1\t\t\tMacchiato\t\t\tP 105")
print ("\t\t\t\t\t\t\t\tA2\t\t\tCapuccino\t\t\tP 95")
print ("\t\t\t\t\t\t\t\tA3\t\t\tIced Coffee\t\t\tP 75")
print ("\t\t\t\t\t\t\t\tA4\t\t\tHot Choco\t\t\tP 65")

print ("\n\n \t\t\t\t\t\t----------------------------------------------------\n\n")


order=eval(input("How many orders do you want to purchase?"))

for i in range (order):
    code=eval(input("Type the code of your choice:"))
    quantity=eval(input("Type the quantity of your order:"))
    
    if code==A1:
        p1=105*quantity
        print (A1, "---", P1, "x", quantity, "=", p1)
        
    elif code==A2:
        p2=95*quantity
        print (A2, "---", P2, "x", quantity, "=", p2)
    
    elif code==A3:
        p3=75*quantity
        print (A3, "---", P3, "x", quantity, "=", p3)
         
    elif code==A4:
        p4=65*quantity
        print (A4, "---", P4, "x", quantity, "=", p4)
        
    else:
        print ("The order does not exist.")
    
total=p1+p2+p3+p4
print ("\nTotal Purchase: P",total)


pay=eval(input ("Payment Amount: P " ))
if pay<total:
    print("Insufficient Amount.")
    pay=eval(input ("Payment Amount: P"))
    
print ("Your change: P", pay-total)
print ("Thank you and come again!")