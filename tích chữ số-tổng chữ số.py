import math
t=int(input())
while t>0:
	t-=1
	s=input()
	kt=0
	Sum=0
	Mul=1
	for i in range(0,len(s)):
		# print(s[i]!=s[len(s)-1])
		if i%2==0 and int(s[i])!=0:
			kt=1
			Mul*=int(s[i])
		if i%2!=0:
			Sum+=int(s[i])
	if kt==0:
		Mul=0
	print(Mul,end=' ')
	print(Sum)
