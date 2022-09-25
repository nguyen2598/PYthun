# s=""
# t=4
while True:
# while t>0:
# 	t-=1
	try:
		s=input()
		kt=0
		for i in s.split():
			i=i.lower()
			if kt==0:
				i=i.capitalize()
				kt=1
			if i[len(i)-1]=='.' or i[len(i)-1]=='?' or i[len(i)-1]=='!' :
				i=i.strip(i[len(i)-1])
				kt=0
			print(i,end='')
			if kt==0:
				print("")
			else:
				print("",end=' ')
	except EOFError: 
		break
