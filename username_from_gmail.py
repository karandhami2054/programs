# email = input("Enter your email:")
# username = email[:email.index("@")]
# print(username)


email = "karan@gmail.com"

position = email.find("@")
# print(position)
# print(email.index("@"))
# print(email.split("@")[1])
username = email[:position]

print(username)