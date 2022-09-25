s=input()
Set={}
i=0
while(i<len(s)-1):
	ss=s[i:i+2];
	if int(ss) not in Set:
		Set[int(ss)]=1
	i+=2
Set=sorted(Set)
for i in Set:
	print(i, end=' ')
	