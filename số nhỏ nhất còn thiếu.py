def GCD(a,b):
	if b==0:return a
	return GCD(b,a%b)

T = int(input())
a=[int(j) for j in input().split()]
Min=min(a)
Max=max(a)
kt=0
for j in range(1,Max+2):
	if j not in a:
		print(j)
		kt=1
		break
