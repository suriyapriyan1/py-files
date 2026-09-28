#number output.
"""
print("<<<<<<<<<<<<>>>>>>>>>>>>")

print(int(10 + 5 * 2))
print(int(20 - 6 / 2))
print(int(2 + 3 * 4 ** 2))
print(int(10 + 2 > 5))
print(int(5 + 3 * 2 == 11))
print(int(10 > 5 and 4 < 2))
print(int(10 + 5 > 12 and 3 * 2 == 6))
print(int(5 << 2 + 1))
print(int(8 + 4 >> 1))
print(int(10 > 5 or 3 + 2 * 2 == 7))
print(int(not (16 >> 2 < 5) or 3 * 2 ** 2 == 12))
print(int(not(4 + 2 * 3 == 10) and (3 << 2) > (16 >> 1)))

print("<<<<<<<<<<<<<>>>>>>>>>>>>>")
#use boolean value.

print("x---------x-----------x-----------x------------x--------x")
print(10 + 5 * 2)
print(20 - 6 / 2)
print(2 + 3 * 4 ** 2)
print(10 + 2 > 5)
print(5 + 3 * 2 == 11)
print(10 > 5 and 4 < 2)
print(10 + 5 > 12 and 3 * 2 == 6)
print(5 << 2 + 1)
print(8 + 4 >> 1)
print(10 > 5 or 3 + 2 * 2 == 7)
print(not (16 >> 2 < 5) or 3 * 2 ** 2 == 12)
print(not(4 + 2 * 3 == 10) and (3 << 2) > (16 >> 1))

print("x------x-----------x------------x-----------x----------x")

#cenima process.

print("WELLCOME TO CENIMA")
customer_name=input("enter customer name:")

number_of_adult_tickets=int(input("number of adult tickets:"))
adult_ticket_price=(500*number_of_adult_tickets)

no_of_child_ticket=int(input(" no of child tickets:"))
child_ticket_price=(250*no_of_child_ticket)

no_of_popcorn=int(input("no of popcorn:"))
popcorn_price=(50*no_of_popcorn)

print("adult_ticket_price:",adult_ticket_price)
print("child_ticket_price:",child_ticket_price)
print("popcorn_price:",popcorn_price)

"""

age=int(input("enter your age: "))

if (age<0):
 if(age<=5):
    print("ticket is free")    
elif(age<=17):
    print("ticket is 100")
elif(age<=59):
    print("ticket is 300")
else:
    print("ticket is 120")    
    