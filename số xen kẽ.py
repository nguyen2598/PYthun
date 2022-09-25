import math
t=int(input())
while t>0:
	t-=1
	s=input()
	kt="YES"
	if len(s)%2==0 or len(s)<2 or s[0]==s[1]:
		kt="NO"
	for i in range(0,len(s)):
		# print(s[i]!=s[len(s)-1])
		if i%2==0 and s[i]!=s[len(s)-1]:
			kt="NO"
			break
	print(kt)
