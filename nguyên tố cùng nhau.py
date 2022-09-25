def GCD(a,b):
	if b==0:
		return a
	return GCD(b,a%b)
n,k=[int(i) for i in input().split()]
en=1
while k>0:
	en*=10
	k-=1
dem=0
for i in range(en//10,en):
	if GCD(i,n)==1:
		dem+=1
		print(i,end=' ')
		if dem==10:
			print("")
			dem=0