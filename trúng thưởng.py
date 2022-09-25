t=int(input())
while t>0:
	t-=1
	a=[0]*1004
	Min=0
	n=int(input())
	for i in range(n):
		s=input()
		a[int(s)]+=1
		if(a[int(s)]>a[Min] or (a[int(s)]==a[Min] and int(s)<Min)):
			Min=int(s)
	print(Min)