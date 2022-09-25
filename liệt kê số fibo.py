t=int(input())
f=[1]*94
f[0]=0
for i in range(2,94):
	f[i]=f[i-1]+f[i-2]
while t>0:
	t-=1
	a,b=[int(i) for i in input().split()]
	for i in range(a,b+1):
		print(f[i],end=' ')
	print("")