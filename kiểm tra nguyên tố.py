import math
def nt(n):
	if n<2:
		return "NO"
	for i in range(2,int(math.sqrt(n))+1):
		if n%i==0:
			return "NO"
	return "YES"

t=int(input())
while t>0:
	t-=1
	s=input()
	ss=0
	if len(s)<4:
		ss=int(s)
	else:ss=int(s[len(s)-4:])
	print(nt(ss))