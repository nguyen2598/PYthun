import math
def nt(n):
	if n<2:
		return 0
	for i in range(2,int(math.sqrt(n))+1):
		if n%i==0:
			return 0
	return 1

t=int(input())
while t>0:
	t-=1
	s=input()
	ss=0
	kt=0
	for i in range(0,len(s)):
		if (i%2==0 and int(s[i])%2!=0) or (i%2!=0 and int(s[i])%2==0) :
			kt=1
			break
		ss+=int(s[i])
	if kt==1 or nt(ss)==0:
		print("NO")
	else:
		print("YES")