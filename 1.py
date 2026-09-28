student_name = input("Student Name: ")
c1 = int(input("Combo 1 Quantity: "))
c2 = int(input("Combo 2 Quantity: "))
c3 = int(input("Combo 3 Quantity: "))
c4 = int(input("Combo 4 Quantity: "))
amount_paid = int(input("Amount Paid: "))

Com1 = c1 * 180
Com2 = c2 * 250
Com3 = c3 * 150
Com4 = c4 * 220

total_combos = c1 + c2 + c3 + c4
total_bill = Com1 + Com2 + Com3 + Com4
balance = amount_paid - total_bill

print("========================================")
print("           COLLEGE CANTEEN              ")
print("               BILL                     ")
print("========================================")
print("Student Name       :",student_name)
print("combo 1            :",c1, "180", Com1)
print("combo 2            :",c2, "250", Com2)
print("combo 3            :",c3, "150", Com3)
print("combo 4            :",c4, "220", Com4)
print("----------------------------------------")
print("Total Combos       :",total_combos)
print("Total Bill         :",total_bill)
print("Amount Paid        :",amount_paid)
print("Balance            :",balance)
print("========================================")
print("       THANK YOU! VISIT AGAIN           ")
print("========================================")
