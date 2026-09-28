# combo
"""
student_name = input("Student Name: ")
c1 = int(input("Combo 1 Quantity: "))
c2 = int(input("Combo 2 Quantity: "))
c3 = int(input("Combo 3 Quantity: "))
c4 = int(input("Combo 4 Quantity: "))
amount_paid = int(input("Amount Paid: "))

cost1 = c1 * 180
cost2 = c2 * 250
cost3 = c3 * 150
cost4 = c4 * 220

total_combos = c1 + c2 + c3 + c4
total_bill = cost1 + cost2 + cost3 + cost4
balance = amount_paid - total_bill

print("========================================")
print("           COLLEGE CANTEEN              ")
print("               BILL                     ")
print("========================================")
print("Student Name       :", student_name)
print("Combo 1            :", c1, "x ₹180 = ₹", cost1)
print("Combo 2            :", c2, "x ₹250 = ₹", cost2)
print("Combo 3            :", c3, "x ₹150 = ₹", cost3)
print("Combo 4            :", c4, "x ₹220 = ₹", cost4)
print("----------------------------------------")
print("Total Combos       :", total_combos)
print("Total Bill         : ₹", total_bill)
print("Amount Paid        : ₹", amount_paid)
print("Balance            : ₹", balance)
print("========================================")
print("       THANK YOU! VISIT AGAIN           ")
print("========================================")

#ATM withdrawal

balance = float(input("Enter account balance: "))
withdraw = float(input("Enter withdrawal amount: "))

if withdraw <= balance:
    print("Withdrawal Successful")
else:
    print("Insufficient Balance")


#online order dilivery.

order_amount = float(input("Enter order amount: "))

if order_amount >= 500:
    print("Delivery is Free")
else:
    print("Delivery charge is ₹50")

#smart door lock

correct_pin = 2468
entered_pin = int(input("Enter 4-digit PIN: "))

if entered_pin == correct_pin:
    print("Door Unlocked")
else:
    print("Incorrect PIN")

#mobile recharge

recharge_amount = float(input("Enter recharge amount: "))

if recharge_amount >= 5000:
    print("Recharge Successful")
else:
    print("Minimum Recharge Amount is ₹5000")

# five problem finish.
"""

name="Adithya"
sixth_letter=name[5]
print("sixth_letter",sixth_letter)

#[number starts from o so {0,1,2,3,4,5,6,7,8,9},name {a,d,i,t,h,y,a}]