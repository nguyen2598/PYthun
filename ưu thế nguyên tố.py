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
	dem=0
	for i in s:
		if nt(int(i))=="YES":
			dem+=1
	Len=len(s)
	kt= "YES" if (dem>len(s)//2) else "NO"
	kq="YES" if nt(Len)== "YES" and kt== "YES" else "NO"
	print(kq)