a=(input("enter the numberof list"))
a=a.split(" ")
a=list(map(int,a))
print(a)
b=[x*x for x in a if x>0]
print(b)
c=[x for x in a if x>=0]
print(c)
word=input("enter the word")
print(word)
vowels=["a","e","i","o","u"]
d=[x for x in word if x in vowels]
print("vowels is",d)
