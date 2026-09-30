
    
def recursion(a):
    if a == 0:
        return 1
    return a * recursion(a-1)


print(recursion(5))

