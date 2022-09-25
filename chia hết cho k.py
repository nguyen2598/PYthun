a,k,n=[int(i) for i in input().split()]
kt=0
m=a
a=(a//k)+1
b=(n//k)+1
for i in range(a,b):
		print(i*k-m,end=' ')
		kt=1
if kt==0:
	print("-1")