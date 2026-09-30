cities = ["Kanchanpur", "Dhanghadi", "Martadi", "doti", "dipayal"]
def func_list(city):
    num = len(city)
    return num

print(func_list(cities))


#print element of list in single line

cities = ["Kanchanpur", "Dhanghadi", "Martadi", "doti", "dipayal"]
def func_list(city):
    c = " ".join(city)
    print("type of c", type(c))
    a = c.split()
    print(a)
    print("type of a", type(a))

    return c


print(func_list(cities))


