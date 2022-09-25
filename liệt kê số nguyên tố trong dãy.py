import math
def nt(n):
	if n<2 :return 0
	for i in range(2,int(math.sqrt(n))+1):
		if n%i==0:
			return 0
	return 1
Set={}
T = int(input())
a=[int(j) for j in input().split()]
kt=0
for j in a:
	if nt(j):
		if j in Set:
			Set[j]+=1
		else:
			Set[j]=1
for i in Set:
	print(i,end=' ')
	print(Set[i])