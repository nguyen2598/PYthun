from math import gcd
l,r=[int (i) for i in input().split()]
for i in range(l,r+1):
	for j in range(i+1,r+1):
		for z in range(j+1,r+1):
			if gcd(i,j)==1 and gcd(i,z)==1 and gcd(z,j)==1:
				print('(',end='')
				print(i,end=', ')
				print(j,end=', ')
				print(z,end=')')
				print("")