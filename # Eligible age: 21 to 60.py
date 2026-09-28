# Eligible age: 21 to 60
# Minimum monthly income: ₹30,000
# Minimum credit score: 700
"""
Eligible_age=int(input("enter customer age: "))
monthly_income=float(input("monthly income: "))
credit_score=float(input("credit score: "))

if 21<= Eligible_age <=60:
    if monthly_income >= 30000:
        if credit_score >=700:
            print("your loan approved")
        else:
            print("credit score is low - loan is rejected")
    else:
        print("monthly income is low - loan is rejected") 
else:
    print("your age is below 21 so - loan is rejected")                   

#Sample Input:

#Enter first number: 45
#Enter second number: 78
#Enter third number: 32

num1=float(input("first number: "))
num2=float(input("second number: "))
num3=float(input("third number: "))

if (num1>=num2) and (num1>= num3):
    print("largest number is : num 1")
elif (num2>=num1) and (num2>=num3):
    print("largest number is : num2")
else:
    print("largest number is : num3")    
    


#Sample Input:

#Enter first number: 45
#Enter second number: 78
#Enter third number: 62

num1=float(input("first number: "))
num2=float(input("second number: "))
num3=float(input("third number: "))

if (num1>num2 and num1<num2) or (num1<num3 and num1>num3):
    print ("second largest nubmer is", num1 )
elif (num2>num1 and num2<num1) or (num2<num3 and num2>num3):
    print ("second largest nubmer is", num2 )
else:
     print("second largest nubmer is", num3 )         


#Sample Input:

#Enter a three-digit number: 583

num1=float(input("first number: "))
num2=float(input("second number: "))
num3=float(input("third number: "))

if num1>num2:
    num1, num2 = num2, num1
elif num1>num3:
    num1, num3 = num3, num1    
elif num2>num3:
    num2, num3 = num3, num2     

print("second largest number ", num2)
print("third largest (smallest) number", num1)    



#Sample Input:

#Enter a three-digit number: 583

number=int(input("enter three digit number : "))

hundred=(number // 100)
tense=(number // 10)%10
units=(number % 10)

if (hundred>=tense) and (hundred>= units):
    print("largest number is  hundred:", hundred)

elif (tense>=hundred) and (tense>= units):
    print("largest number is  tense:", tense)

else:
    print("largest number is  units:", units)    
    
# we are finally completed five problems.
"""

name="Adithya"
sixth_letter=name[5]
print("sixth_letter",sixth_letter)

#[number starts from o so {0,1,2,3,4,5,6,7,8,9},name {a,d,i,t,h,y,a}]