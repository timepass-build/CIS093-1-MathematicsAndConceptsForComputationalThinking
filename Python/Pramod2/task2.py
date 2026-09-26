# Grade Calculator

math = int(input("Input your marks in math/100: "))
english = int(input("Input your marks in english/100: "))
computer = int(input("Input your marks in computer/100: "))
business = int(input("Input your marks in business/100: "))
marketing = int(input("Input your marks in marketing/100: "))

totalmarks = math + english + computer + business + marketing

print(f"Your total marks is {totalmarks}")

average = totalmarks / 5

print(f"Your average marks is {average}")

if average < 50 or math < 50 or english < 50 or computer < 50 or business < 50 or marketing < 50:
    print("F")

elif average < 60:
    print("D")

elif average < 70:
    print("C")

elif average < 80:
    print("B")

else:
    print("A")


    