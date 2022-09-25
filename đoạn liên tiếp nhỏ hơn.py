t=int(input())
while t>0:
	t-=1
	n=int(input())
	a=[int(i) for i in input().split()]
	st=[]
	print('1',end=' ')
	st.append(0)
	for i in range(1,n):
		while(len(st)>0 and a[i]>=a[st[-1]]):st.pop()
		if len(st)==0:print(i+1,end=' ')
		else:print(i-st[-1],end=' ')
		st.append(i)
	print('')