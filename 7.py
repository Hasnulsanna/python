l1=[]
l2=[]
l3=[]
x=int(input("enter the length of list 1"))
for i in range(x):
   l1.append(input("enter the element of l1"))
   l1=list(map(int,l1))
print(l1)
y=int(input("enter the length of list 2"))
for i in range(y):
   l2.append(input("enter the element of l2"))
   l2=list(map(int,l2))
print(l2)
if len(l1)==len(l2):
   print("same length")
else:
   print("different length")
if sum(l1)==sum(l2):
   print("sum is same")
else:
   print("sum is different")
def duplicate(l1,l2):
   l3=[x for x in l1 if x in l2]
   return l3
print("duplicate elements are",duplicate(l1,l2))


