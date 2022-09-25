P="ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
while True:
	s=input()
	if s=="0":
		break
	a=s.split()
	k=int(a[0])
	s=a[1]
	ss=""
	for i in s:
		ss=P[(P.index(i)+k)%28]+ss
	print(ss)