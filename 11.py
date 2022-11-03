def countofa(l1):
    b=l1.split(" ")
    count=0
    for i in range(0,len(b)):
        if(b[i]==word):
            count=count+1
    return count
word='a'
l1=[]
l1=input("enter the word")
print(countofa(l1))
