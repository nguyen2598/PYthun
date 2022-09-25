t=int(input())
while t>0:
	t-=1
	dem=0
	n=int(input())
	while dem<1001:
		dem+=1
		if n%7==0:
			print(n)
			break
		s=n+int(str(n)[::-1])
		n=s

	