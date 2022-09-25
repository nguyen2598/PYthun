def MOD(n,k):
	x=int(2**(n-1))
	# print(x,k)
	if k==x:
		return chr(ord('@')+n)
	elif k>x:
		return MOD(n-1,k-x)
	else:
	    return MOD(n-1,k)
t=int(input())
while t>0:
	t-=1
	n,k=[int(i) for i in input().split()]
	s=str(MOD(n,k))
	print(s)