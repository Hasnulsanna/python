Python 3.5.2 (default, Jan 26 2021, 13:30:48) 
[GCC 5.4.0 20160609] on linux
Type "copyright", "credits" or "license()" for more information.
>>> num=int(input("enter a number"))
enter a number7
>>> factorial=1
>>> if num<0;
SyntaxError: invalid syntax
>>> if num<0:
	print("no factorial")
elif num == 0:
	print("factorial of 0 is 1")
else:
	for i in range(1,num+1):
		factorial=factorial*i
	print("factorial of",num,"is",factorial)

	
factorial of 7 is 5040
>>> 
