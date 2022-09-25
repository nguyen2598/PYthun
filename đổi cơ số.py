c=[0,1,2,3,4,5,6,7,8,9,"A", "B", "C", "D", "E", "F", "G", "H", "I" ,"J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U","V", "W", "X", "Y", "Z"]
t=int(input())
while t>0:
	t-=1
	s=input().split()
	n=int(s[0])
	b=int(s[1])
	SS=""
	while n>0:
		m=n%b
		n//=b
		SS=str(c[m])+SS
	print(SS)