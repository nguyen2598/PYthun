T = int(input())
for i in range(T):
	n,m=[int(x) for x in input().split()]
	a = []
	s=input()
	for i in s.split():
		a.append(int(i))
	ans = []
	for i in range(m,n):
		print(a[i],end=' ')
	for i in range(m):
		print(a[i],end=' ')
	print('')