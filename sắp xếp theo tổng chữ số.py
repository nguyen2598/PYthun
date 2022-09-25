def cmp(item):
	Sum=0
	for i in str(item):
		Sum*=int(i)
	return (Sum,int(item))
t=int(input())
while t>0:
	t-=1
	n=int(input())
	a=[int(i) for  i in input().split()]
	# a=set(list(a))
	a=sorted(a,key=cmp)
	for i in a:
		print(i,end=' ')
	print("")