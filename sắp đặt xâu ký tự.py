t=int(input())
stt=0
while t>0:
	t-=1
	s=input()
	ss=input()
	s=sorted(s)
	ss=sorted(ss)
	stt+=1
	print("Test",stt,end=': ')

	if s==ss:
		print("YES")
	else:
		print("NO")