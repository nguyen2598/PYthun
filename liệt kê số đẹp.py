import queue
q=queue.Queue()
a=[]

q.put("2")
q.put("4")
q.put("6")
q.put("8")
while True:
	s=q.get()
	if len(s)==5:
		break
	q.put(s+"0")
	q.put(s+"2")
	q.put(s+"4")
	q.put(s+"6")
	q.put(s+"8")
	ss=s+s[::-1]
	a.append(ss)
t=int(input())
while t>0:
	t-=1
	m=int(input())
	vt=0
	while True:
		if int(a[vt])>=m:
			break
		print(a[vt],end=' ')
		vt+=1
	print("")
