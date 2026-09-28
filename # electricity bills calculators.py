# electricity bills calculators

customer_name=input("Enter a customer name:")

units=float(input("units:"))
cost_per_units= 6.50
total_bill=units*cost_per_units

print("cost_per_units:",cost_per_units)
print("total_bill:",total_bill)


#online shopping discount calculator

product_name = input("enter product:")
original_price = float(input("orginal price"))

discount_percentage = float(input("enter discount"))

discount_amount = (original_price * discount_percentage) / 100
final_price = original_price - discount_amount

print("Product_name:",product_name)
print("Original Price:",original_price)
print("Discount:",discount_percentage)
print("Discount Amount:",discount_amount)
print("Final Price:",final_price)


#mobile datausage calculator

user_name = input("enter user name")
data_used = float(input("enter data usage"))
cost_per_gb = float(input("cost_per_gb"))

total_data_charge = data_used * cost_per_gb

print("User:",user_name)
print("Data Used:",data_used)
print("Cost per GB:",cost_per_gb)
print("Total Data Charge:",total_data_charge)



#add two numbers

a = int(input("enter first num:"))
b = int(input("enter second num:"))

sum_val = a + b
difference_val = a - b
product_val = a * b

print("Sum:",sum_val)
print("Difference:",difference_val)
print("Product:",product_val)



#problem describtion


vehicle_number = input("enter vehicle_number:")
hours_parked = int(input("enter hours parked"))
cost_per_hour = float(input("enter cost per hours:"))
discount_amount = float(input("enter discount amount:"))

parking_fee = hours_parked * cost_per_hour
final_amount = parking_fee - discount_amount

print("Vehicle:",vehicle_number)
print("Parking Fee:",parking_fee)
print("Discount_amount:",discount_amount)
print("Final Amount:",final_amount)

