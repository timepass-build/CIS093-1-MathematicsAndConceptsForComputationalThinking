# List Uniqueness Checker

items = ["apple", "banana", "orange", "apple", "mango"]

seen = []
duplicate_found = False

for item in items:
    if item in seen:
        print(f"Duplicate element: {item}")
        duplicate_found = True
        break
    else:
        seen.append(item)

if not duplicate_found:
    print("All elements are unique.")