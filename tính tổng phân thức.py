t=int(input())
while t>0:
	t-=1
	n=int(input())
	x=1
	s=0
	if n%2==0:
		x=2
	for i in range(x,n+1,2):
		s+=1/i;
	print('%.6f' % s)