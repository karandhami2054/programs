nepali = {
    "mother": "आमा",
    "father": "बुवा",
    "brother": "भाई",
    "sister": "बहिनी",
    "ram": "राम",
}

user = input("Enter your word to convert in nepali: ").lower()
print(nepali.get(user, "Data not found."))

