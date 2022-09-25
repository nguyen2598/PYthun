s=input()
a=s[len(s)-3:len(s)]
a=a.lower()
if a==".py":
	print("yes")
else:
	print("no")