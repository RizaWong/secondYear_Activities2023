code1 = "ABC123"
code2 = "XYZ456"

print ('Welcome to the Discount Calculator!')

while True:
    purchase_amount = eval (input ("Enter the purchase amount [0 to terminate]: P "))

    if purchase_amount == 0:
        print ("Program Terminated.")
        break 

    else:
        coupon_code = input ("Enter the coupon code [ABC123 for 10% off or XYZ456 for 20% off]: ")

        if coupon_code == code1:
            dc_applied = purchase_amount * .10
            dc_price = purchase_amount - dc_applied
            print (f"Discount Applied: P {dc_applied}")
            print (f"Discounted Price: P {dc_price}")
        
        elif coupon_code == code2:
            dc_applied = purchase_amount * .20
            dc_price = purchase_amount - dc_applied
            print (f"Discount Applied: P {dc_applied}")
            print (f"Discounted Price: P {dc_price}")
        
        else:
            print ("Invalid coupon code. No discount applied.")
        