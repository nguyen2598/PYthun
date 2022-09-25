t=int(input())
while t>0:
	t-=1
	s=input()
	Sum=0
	for i in s:
		Sum=Sum*10+int(i)
		Sum%=3;
	if Sum==0:
		print("YES")
	else:
		print("NO")

