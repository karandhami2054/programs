sentence = input("Enter your sentence: ").lower()
vowel= "aeiou"
vowel_count = sum(sentence.count(vowel) for vowel in "aeiou")
print(vowel_count)