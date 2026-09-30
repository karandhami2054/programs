string = "Hello i have 25 orange And 15 mangoes."

without_space = ""
for char in string:
    if char.isdigit():
        continue
    elif char.isspace():
        continue
    else:
        without_space += char   

print(without_space) #print without space and digits 


print(string.replace(" ",""))  #print without space only