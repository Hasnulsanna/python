end=int(input("enter the end year"))
for i in range(2022+1,end):
    if(i%4 == 0 and i%100!=0 or i%400 == 0):
        print(i)
