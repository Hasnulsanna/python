a=[1,2,3,-2,4,5,-1]
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
ordinality=input("enter the word")
print("ordinality of the ",ordinality,"is")
e=[ord(x) for x in ordinality]
print(e)
