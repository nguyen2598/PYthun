t=int(input())
while t>0:
	t-=1
	s=input()
	Sum=0
	for i in s:
		Sum+=int(i)
	Sum=str(Sum)
	S=str(Sum[::-1])
	# print(S)
	# print(Sum)
	kt="YES" if S==Sum and len(S)>1 else "NO"
	print(kt)