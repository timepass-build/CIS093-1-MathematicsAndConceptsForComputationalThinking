# Number System Conversion and Number Analysis

num = int(input("Enter a positive integer with at least 3 digits: "))

if num < 0:
    print("Please enter a positive number.")
elif num < 100:
    print("Please enter a number with at least 3 digits.")
else:
    print(f"Decimal: {num}")
    print(f"Binary: {bin(num)}")
    print(f"Octal: {oct(num)}")
    print(f"Hexadecimal: {hex(num)}")

    last_digit = num % 10
    print("Last digit:", last_digit)

    if num % 2 == 0:
        print("Number is Even")
    else:
        print("Number is Odd")