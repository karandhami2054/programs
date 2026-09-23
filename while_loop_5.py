# WAP to check and display a number if found using while loop 
square = (1, 4, 9, 16,25, 36, 49, 64, 81, 100)
user = int(input("Enter any number: "))
i = 0
while i < len(square):
    if square[i] == user:
        print("Found at index", i)
        break
    else:
        print("Finding...")
    i +=1