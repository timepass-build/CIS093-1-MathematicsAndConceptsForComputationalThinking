# String ASCII Capitalization

text = input("Enter a string with at least 8 characters: ")
text = text.lower()

if len(text) < 8:
    print("Please enter a string with at least 8 characters.")
else:
    result = ""

    for i in range(len(text)):
        if i % 2 == 0:
            ascii_value = ord(text[i])

            if 97 <= ascii_value <= 122:
                ascii_value = ascii_value - 32

            result = result + chr(ascii_value)
        else:
            result = result + text[i]

    print(result)