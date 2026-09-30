# paragraph = "The quick brown fox jumps over the lazy dog. The dog was not that lazy, really.".lower()
# word = input("Enter your word: ").lower()
# print(paragraph.count(word))


# email = "student@gmail.com"
# user=""
# for a in email:
#     if a == "@":
#         break
#     else:
#         user +=a

# print(user)


sentence = "hello (nepal) world"
word = ""
for a in sentence:
    if a == "(" or ")":
        break
    else:
        word +=a
        print(word)
print(word)


