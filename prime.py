n=10
numbers=range (1,n)
for x in numbers:
	if n % x == 0:
		print("Not prime")
	else:
		print("Prime")