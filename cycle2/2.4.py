from math import sqrt

def even(n):
	string = str(n)
	for digit in string:
		if digit in '13579':
			return False
	return True

def square(n):
	a = sqrt(n)
	b = int(sqrt(n))
	if(a==b):
		return True
	else:
		return False

start=int(input("enter start number:"))
end=int(input("enter ending number:"))
if len(str(start))!=4 and len(str(end))!=4:
	print("invalid")
for i in range(start,end):
	if(even(i) and square(i)):
		print(i)



