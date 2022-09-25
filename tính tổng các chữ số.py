t=int(input())
while t>0:
	t-=1
	n=input()
	x=1
	s=""
	ss=""
	Sum=0
	for i in n:
		if i<'0' or i>'9':
			s+=i
		else:
			Sum+=int(i)
	s=sorted(s)
	for i in s:
		ss+=i
	ss+=str(Sum)
	print( ss)