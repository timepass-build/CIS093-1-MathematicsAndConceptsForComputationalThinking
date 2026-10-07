choice = int(input("Enter: "))

while choice != 4:
    if choice == 1:
        print("Hello")
    elif choice == 2:
        print("You have pressed 2")
    elif choice == 3:
        print("You have pressed 3")
    else:
        print("You pressed number higher than 4")
    choice = int(input("Enter: "))

print("Invalid!")