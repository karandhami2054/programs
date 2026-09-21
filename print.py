import time
def usingFunctions(): 
    count =0 
    while count<10: 
        print("\rmrcet cse dept ",count, end="") 
        time.sleep(1)
        count=count+1 
 
usingFunctions() 

for i in range(10):
    print("Hello\r world\r", i)