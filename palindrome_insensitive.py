sentence = input("Enter your sentence: ")
temp= sentence.replace(" ", "").lower()
if temp == temp[::-1]:
    print("Palindrome: ")
else:
    print("NOt Palindrome: ")


