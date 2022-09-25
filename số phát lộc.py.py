t=int(input())
while t>0:
	t-=1
	s=input()
	a=s[len(s)-2:len(s)]

	if a=="86":
		print("YES")
	else:
		print("NO")