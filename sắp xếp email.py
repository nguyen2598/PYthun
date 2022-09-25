f = open("CONTACT.in",'r',encoding = 'utf-8')
b = f.readlines()
Set=[]
for i in range(len(b)):	
	if len(b[i])!=0 and b[i]!='\n':
		# print(len(b[i]))
		b[i]=b[i].lower()
		b[i]=b[i].replace('\n','')
		if b[i] not in Set:
			Set.append(b[i])
Set=sorted(Set)
for i in Set:
	print(i)