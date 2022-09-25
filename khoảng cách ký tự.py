import math
t=int(input())
while t>0:
	t-=1
	s=input()
	ss=s[::-1]
	kt="YES"
	for i in range(1,len(s)):
		# print(ord(s[i])-ord(s[i-1]))
		if abs(ord(s[i])-ord(s[i-1]))!=abs(ord(ss[i])-ord(ss[i-1])):
			kt="NO"
			break
	print(kt)
