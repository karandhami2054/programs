string = "Hello i have 25 orange and 15 mangoes."

number = ""
for char in string:
    if char.isdigit():
        number += char

    elif number:
        print(number)
        number = ""

