S1S=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
t=int(input())
while t>0:
	t-=1
	n=int(input())
	s=input()
	s=s[::-1]
	ss=""
	dem=0
	if n==2:Max=1
	elif n==4:Max=2
	elif n==8:Max=3
	else :Max=4
	# print(Max)
	Sum=0
	for i in range(len(s)):
		
		Sum+=(int(s[i])*(2**dem))
		# print("s",Sum,dem)
		dem+=1
		if((dem==Max) or i+1==len(s)):
			ss=S1S[Sum]+ss
			Sum=0
			dem=0
	print(ss)