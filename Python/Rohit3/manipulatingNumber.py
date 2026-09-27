import math

num1 = float(input("Enter first number: "))
num2 = float(input("Enter 2nd number: "))

# SUM
print(f"The sum of the two number is {num1 + num2}.")

# Min and Max values
print(f"Min value is {min(num1, num2)}")
print(f"Max value is {max(num1, num2)}")

# Find the power of the first number raised to the second number

print(f"{num1} raised to the power of {num2} is {math.pow(num1, num2)}")