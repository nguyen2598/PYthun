t=int(input())
while t>0:
	s=input()
	dem=1
	for i in range(0,len(s)):
		if i<len(s)-1 and s[i]==s[i+1] :
			dem+=1
		else:
			print(dem,end='')
			print(s[i],end='')
			dem=1
	print("")
	t-=1
			
