a=[0]*30
n,k=[int(i) for i in input().split()]
arr=sorted(list(set({str(i) for i in input().split()})))
n=len(arr)
# print(arr)
def Try(i):
	for j in range(a[i-1]+1,n-k+i+1):
		a[i]=j
		if i==k:IN()
		else: Try(i+1)
def IN():
	for i in range(1,k+1):
		print(arr[a[i]-1],end=' ')
	print("")
Try(1)