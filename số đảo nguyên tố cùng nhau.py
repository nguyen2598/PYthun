def GCD(a,b):
	if b==0:
		return a
	return GCD(b,a%b);

t=int(input())
while t>0:
	t-=1
	n=input()
	s=n[::-1]
	Sum=GCD(int(n),int(s))
	if Sum==1:
		print("YES")
	else :
		print("NO")