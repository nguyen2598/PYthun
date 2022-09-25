s1=input()
s2=input()
vt=int(input())-1
kt=0
for i in range(0,len(s1)):
	if(i==vt):
		print(s2,end='')
		kt=1
	print(s1[i],end='')
if kt==0:
	print(s2,end='')