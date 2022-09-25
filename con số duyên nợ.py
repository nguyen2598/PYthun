t=int(input())
while t>0:
	t-=1
	n=input()
	if n[len(n)-1]==n[0]:
		print("YES")
	else :
		print("NO")