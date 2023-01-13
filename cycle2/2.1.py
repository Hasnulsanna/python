def fact(n):
    if n==1 or n==0:
        return 1
    else:
        return (n*(fact(n-1)))
num =int(input("enter the number"))                
if num<0 :
    print("invalid")
else:
    print("factorial of number is :")
    print(fact(num))
