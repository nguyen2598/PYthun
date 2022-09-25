T = int(input())
Set={}
for i in range(T):
	s=input()
	kt=0
	for j in range(len(s)):
		if((j+2<len(s) and s[j]!=s[j+2]) ):
			kt=1
	if kt==1:
		print("NO")
	else:
		print("YES")