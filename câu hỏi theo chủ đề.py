t=int(input())
dem=0
Set={}
ss=''
while t>0:
	t-=1
	s=input()
	a=s.split()
	if len(a)==0:
		dem=0
	else:
		if dem==0:
			Set[s]=0
			ss=s
		else:
			Set[ss]+=1
		# print(dem,Set[ss])
		dem=1
	
	# print(dem,len(s))
for i in Set:
	print(i,end=': ')
	print(Set[i])