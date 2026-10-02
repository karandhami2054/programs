prime = int(input("Enter a number: "))

for i in range(2, prime):
    if(prime % i != 0):
        print("prime number")
        break;
else:
    print("not prime")



