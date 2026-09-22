def biggest(a,b,c): 
    if a>b and a>c :
        return a
    elif b>c and b>a:
        return b
    else:    
        return c 
        
   
     
a=int(input("Enter a value ")) 
b=int(input("Enter b value ")) 
c=int(input("Enter c value ")) 
big= biggest(a,b,c) 
print("big number= ",big) 