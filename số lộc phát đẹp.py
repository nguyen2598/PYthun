s=input()
kt="YES"
bn=1
i=0
while i<len(s):
	if i+2<len(s) and i+1<len(s) and s[i]=='6' and s[i+1]=='8'and s[i+2]=='8':
		i+=3
		continue
	elif i+1<len(s) and s[i]=='6' and s[i+1]=='8':
		i+=2
		continue
	elif s[i]=='6':
		i+=1
		continue
	kt="NO"
	break
print(kt)