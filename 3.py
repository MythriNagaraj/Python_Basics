'''Find the Largest of Three Numbers
Write a program that takes 3 numbers and prints the largest one.'''
num1=int(input("Enter the first number: "))
num2=int(input("Enter the secind number: "))
num3=int(input("Enter the third number: "))

if num1>=num2 and num1>=num3:
    print("num1 is the largerest number")
elif num2>=num1 and num2>=num3:
    print("num2 is largest number")
else :
    print("num3 is largest number")

'''Check if a Number is Positive, Negative, or Zero
Take an integer from the user and determine whether it's positive, negative, or zero.'''
num1=float(input("enter the number"))

if num1>0:
    print("the shown number is positive")
elif num1<0:
    print("the given number is negative")
else:
    print("the num is equal to 0")

#Write a program that takes a number and returns the sum of its digits.

a=float(input("enter the number: "))
b=float(input("Enter the number: "))
c=float(input("Enter the number: "))

sum=a+b+c
print("the total sum of all the three inputs is :"str(sum))