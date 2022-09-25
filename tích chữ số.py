t=int(input())
while t>0:
	t-=1
	n=input()
	x=1
	s=1
	for i in n:
		if i!='0':
			s*=int(i)
	print( s)