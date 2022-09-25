import math
i=int(input())
while(i>0):
	i-=1
	n,l,m=[float(x) for x in input().split()]
	z=float(math.log(m/n)/(math.log(1+l/100)))
	k=int(z)
	if(z>k):print(k+1)
	else :print(k)