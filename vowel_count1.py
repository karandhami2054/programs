sentence = input("Enter the sentence: ").lower()

vowel = sentence.count("a") + sentence.count("e") + sentence.count("i") + sentence.count("o") + sentence.count("u")
print(vowel)