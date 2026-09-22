


name = input("Enter your full name ")
kara = name.lower().find("r")
if kara == -1:
    print("Your word doesnot have r letter")
else:
    print("have letter in ", kara, "place")

print(name.replace("karan", "Pratik"))