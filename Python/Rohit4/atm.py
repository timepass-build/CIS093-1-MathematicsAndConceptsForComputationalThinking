username = "golden_user"
password = "super_secret_password"

if username == "golden_user": 
    if password == "super_secret_password":
        print("Login Success!")
    else:
        print("use another password")
else:
        print("Login Failed")

balance = 1000
var=input("Enter the amount to withdraw: ")

if int(var) <= balance:
    balance -= int(var)
    print(f"Withdrawal successful! New balance: {balance}") 
else:
    print("Insufficient funds")