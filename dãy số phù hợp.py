
t=int(input())
while t>0:
	t-=1
	n=int(input())
	a=sorted([int(i) for i in input().split()])
	b=sorted([int(i) for i in input().split()])
	# print(a)
	# print(b)
	kt=0
	for i in range(n):
		if(a[i]>b[i]):
			kt=1
			print("NO")
			break;
	if kt==0:
		print("YES")