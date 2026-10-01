user = ['karan', 'dhami', 'is', 'my', 'name', 25, "karan", "dhami"]

print(user)
user.append("pratik")
print(user)

user.extend(["Dhami", 2, "gopal"])
print(user)

user.pop()
print(user)

user.remove(2)
user.remove(25)
print(user)

user.insert(1, "hari")
print(user)

print(user.count("karan"))
print(len(user))

user.sort()
print(user)

print(sorted(user))

user.sort(reverse=True)
print(user)

a = [5, 10, 15, 20, 25, 30]
print(sum(a))
print(max(a))
print(min(a))