b = [True]*100000
c=[0]*1009
z=1
for i in range(2,100000):
	if b[i]:
		c[z]=i
		z+=1
		if z>1004:
			break
		for j in range(2*i,100000,i):
			b[j]=False
t=int(input())
while t>0:
	t-=1
	dem=0
	n=int(input())
	for i in range(5,n-5):
		if((b[i] and b[i+2] and b[i+6]) or (b[i] and b[i+4] and b[i+6])) :
			dem+=1
	print(dem)