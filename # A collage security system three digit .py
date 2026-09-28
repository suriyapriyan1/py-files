# A collage security system three digit value conversion.
"""
The security system considers the middle digit as a hidden verification digit. It should be removed from the code, while the first and last digits are combined to create a new verification number.
"""

three_digit_value=int(input("enter the three-digit value:" ))

first_digit=three_digit_value//100
middle_digit=(three_digit_value//10)%10
last_digit=three_digit_value%10

verification_number=first_digit * 10 + last_digit

print("first_digit:", first_digit)
print("middle_digit:", middle_digit)
print("last_digit:", last_digit)
print("verification_number:", verification_number)

"""
First digit = 5
Middle digit = 8 → Hidden
Last digit = 3
New verification number = 53

"""

"""

Task:
Write a Python program to generate the verification number by removing the middle digit.

Sample Input:

583

"""