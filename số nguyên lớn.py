def GCD(a,b):
	if b==0:
		return a
	else: return GCD(b,a%b)
t=int(input())
while t>0:
	t-=1;
	n=int(input())
	s=input()
	Sum=0
	for i in s:
		Sum=Sum*10+int(i)
		Sum%=n
	print(GCD(n,Sum))