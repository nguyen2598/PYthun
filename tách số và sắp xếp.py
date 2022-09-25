import re
t=int(input())
a=[]
while t>0:
	t-=1
	s=input()
	a+=[int(i) for i in re.findall('\d+',s)]
a=sorted(a)
for i in a:
	print(i)