import math
def GCD(n,m):
	if m==0:
		return n
	else :return GCD(m,n%m)
def nt(n):
	if n<2:
		return 0
	for i in range(2,int(math.sqrt(n))+1):
		if n%i==0:
			return 0
	return 1
def Num(n):
	n=str(n)
	Sum=0
	for i in n:
		Sum+=int(i)
	return Sum
t=int(input())
while t>0:
	t-=1
	a,b=[int(i) for i in input().split()]
	c=int(GCD(a,b))
	# print(Num(c))
	if(nt(Num(c))==1):
		print("YES")
	else:
		print("NO")