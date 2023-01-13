a=(input("enter the numberof list"))
a=a.split(" ")
a=list(map(int,a))
print(a)
b=[x*x for x in a if x>0]
print(b)
c=[x for x in a if x>=0]
print(c)
b=
vowels=["a","e","i","o","u"]
d=[x for x in a if x in vowels]
print("vowels is",d)
