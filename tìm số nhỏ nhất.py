t=int(input())
while t>0:
	s=input()
	Sum=0
	Max=999999
	for i in range(0,len(s)):
		if s[i]>='0' and s[i]<='9': 
			Sum=Sum*10+int(s[i])

		else:
			if(Sum!=0 and Sum<Max):Max=Sum
			Sum=0
		
	if(Sum!=0 and Sum<Max):Max=Sum
	t-=1
	print(Max)