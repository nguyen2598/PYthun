n=str(input())
n=n[::-1]
# print(type(n))
s=""
for i in range(0,len(n)):
	s+=n[i]
	if(i+1)%3==0 and i!=len(n)-1:
		s+=','
	
s=s[::-1]
print(s)

