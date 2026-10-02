username = input("Enter username: ")

if(len(username)<10):
    print("Your username contains less than 10 characters")
elif(len(username)==10):
    print("your username has exactly 10 characters.")
else:
    print("Your username contains more than or equal to 10 characters")