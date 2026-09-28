#security code five digit

five_digit_number =int(input("enter a five digit number:"))

d1=five_digit_number//10000
d2=(five_digit_number//1000)%10
d3=(five_digit_number//100)%10
d4=(five_digit_number//10)%10
d5=five_digit_number%10

security_code = d1 * 10000 + d2 * 1000 + d3 * 100 +d4 * 10 + d5
print("Security Code:", security_code)

Digit_sum = d1 + d2 + d3 + d4 + d5
digit_product = d1 * d2 * d3 * d4 * d5
reverse_code = d5 * 10000 + d4 * 1000 + d3 * 100 + d2 * 10 + d1
difference = five_digit_number - reverse_code
first_last_equal = d1 == d5

print("Digit_sum:",Digit_sum)
print("Digit_product:",digit_product)
print("Reverse_code:",reverse_code)
print("Difference:",difference)
print("First and last digits equal:",first_last_equal)

#Write a Python program to perform the above Five-Digit Analyzer operations.