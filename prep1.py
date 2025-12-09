# Easy (Warm-Up)

print("Hello, World!")

# Odd or Even
num = int(input("Enter number:"))
if num % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")    

# Largest of Three Numbers
# Take 3 numbers as input and print the largest.
a = int(input("Enter 1st number:"))
b = int(input("Enter 2nd number:"))
c = int(input("Enter 3rd number:"))

largest = max(a,b,c)
print(f"The largest number is: {largest}")

# Sum of N Natural Numbers
# Input: N → Output: Sum = 1 + 2 + ... + N

n = int(input("Enter number:"))
sum = n*(n+1)//2
print("Sum",sum)

# Leap Year Checker
# Check if the given year is a leap year.
year = int(input("Enter year"))
if (year % 4 == 0):
    print("The year is leap year")
else:
    print("The year is not leap year")

# Simple Interest Calculator
# Formula: (P × R × T) / 100
x = float(input("Enter principle amount"))
y = float(input("Enter Rate"))
z = float(input("Enter Time(In Years)"))

formula = (x*y*z)/100

print("The simple interest is:", formula)

# Swap Two Numbers Without a Temp Variable
# Use arithmetic or tuple unpacking.

p = int(input("Enter first number (a):"))
s = int(input("Enter second number (b):"))

print (f"/nBefore swapping: a = {p}, b = {s}")

p, s = s, p
print(f"After swapping: a = {p}, b = {s}")