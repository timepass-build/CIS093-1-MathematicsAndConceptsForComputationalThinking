
password = input("Enter password: ").lower()

while password != 'admin123':
    password = input("Wrong Password. Try again: ")

print("Login successful.")