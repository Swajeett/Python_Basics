# Check if number is even
for i in range(0, 20, 2):
    print(i)

# Print numbers from 1 to 50    
for i in range(1, 51):
    print(i)

# Print only even numbers between 1 and 100
for i in range(2, 101, 2):
    print(i)

# Reverse countdown
for i in range(20, 0, -1):
    print(i)

# Sum of first N numbers
N = int(input("Enter a number: "))
total = 0

for i in range(1, N + 1):
    total += i

print("Sum =",total)

# Multiplication Table
num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=",num*i)