def calculateRoomServiceGST(a, b):
    return(a+b)*1.18

def calculateDiningGST(c, d):
    return(c+d)*1.13

def calculateLaundryGST(e):
    return e*1.07

def totalBill(a, b, c, d, e):
    return (calculateRoomServiceGST(a, b) + calculateDiningGST(c, d) + calculateLaundryGST(e))

def calculateDiscountedBill(a, b, c, d, e):
    total= totalBill(a, b, c, d, e) 
    discount= total*0.20
    return total - discount

total = totalBill(100, 100, 100, 100, 100) 
discount = total * 0.20 
payable = calculateDiscountedBill(100, 100, 100, 100, 100) 

print(f"Total after GST = {total:.2f}") 
print(f"Discount = {discount:.2f}") 
print(f"Final payable amount = {payable:.2f}")