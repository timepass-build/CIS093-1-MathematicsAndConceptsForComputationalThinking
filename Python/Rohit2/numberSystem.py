# Number System Conversation in Python

# DECIMAL

num1 = input("Enter your number: ")
forDec = int(num1)

print("*" * 50)
print(f"Your Number is {num1}")
print("*" * 50)

print("\nDecimal")
print("-" * 50)

# Decimal to binary
print(f"Decimal to Binary:      {bin(forDec)}")

# Decimal to Hexa
print(f"Decimal to Hexa:        {hex(forDec)}")

# Decimal to Octal
print(f"Decimal to Octal:       {oct(forDec)}")


# Binary
print("-" * 50)
print("Binary")
print("-" * 50)

# Binary to Decimal
forBin = f"{num1}"
num2 = int(forBin, 2)
print(f"Binary to Decimal:{num2}")

# Binary to Hexa
print(f"Binary to Hexa:{hex(num2)}")

# Binary to Octal
print(f"Binary to Octal:{oct(num2)}")


# Hexadecimal
print("-" * 50)
print("Hexadecimal")
print("-" * 50)

# Hexadecimal to Binary
num2 = f"{num1}"
num3 = int(num2, 16)
print(f"Hexa to Binary:        {bin(num3)}")

# Hexadecimal to Decimal
print(f"Hexa to Decimal:       {int(num2, 16)}")

# Hexadecimal to Octal
print(f"Hexa to Octal:         {oct(num3)}")

# Octal
print("\n" + "-" * 50)
print("Octal")
print("-" * 50)

# Octal to Decimal
num2 = f"{num1}"
num3 = int(num2, 8)
print(f"Octal to Decimal:      {num3}")

# Octal to Binary
print(f"Octal to Binary:       {bin(num3)}")

# Octal to Hexadecimal
print(f"Octal to Hexa:         {hex(num3)}")

print("*" * 50)
print("CONVERSION COMPLETE!")
print("*" * 50)