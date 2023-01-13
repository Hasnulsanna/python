def word(c):
    biggest=0
    longest=" "
    for i in c:
        count=0
        for j in i:
            count=count+1
            if(biggest<count):
                biggest=count
                longest=i
    print("The longest string is"+longest)
    print("The length of longest string is",biggest)
c=[]
n=int(input("size of the list?"));
for i in range(n):
    b=c.append(input("enter the words in the list"));
print(c)
word(c)
