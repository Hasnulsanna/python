def pattern(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print("*",end=" ")
        print()
    for i in range(n,0,-1):
        for j in range(0,i-1):
            print("*",end=" ")
        print()
   
num=int(input("number of steps"));
pattern(num)
        
