
    
def recursion(a):
    if a == 0:
        return 0
    return a + recursion(a-1)


print(recursion(5))

