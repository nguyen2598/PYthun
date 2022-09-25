n,k=[int(i) for i in input().split()]
b={int(i) for i in input().split()}
b=list(set(b))
b=sorted(b)
a=[0]*50
n=len(b)
def In():
	for i in range(1,k+1):
		print(b[a[i]-1],end=' ')
	print("")
def Try(i):
	for j in range(a[i-1]+1,n-k+i+1):
		a[i]=j;
		if i==k:In();
		if i<k: Try(i+1);

Try(1)