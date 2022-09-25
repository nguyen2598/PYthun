def xuly():
	n=int(input())
	tmp,dem=0,1
	while n//10!=0:
		tmp=(n%10+tmp>=5)
		# print(tmp+1)
		n//=10
		dem*=10
	print((n+tmp)*dem)
t=int(input())
while t>0:
	t-=1
	xuly()