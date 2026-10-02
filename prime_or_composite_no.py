prime = int(input("Enter your number: "))

for i in range(2, prime):
    if (prime % i) == 0:
        print("composite number")
        break

else:
    print("prime number")

    