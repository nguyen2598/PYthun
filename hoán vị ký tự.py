from itertools import permutations

s=input()
arr=permutations(s)
for i in arr:
	print(''. join (i))