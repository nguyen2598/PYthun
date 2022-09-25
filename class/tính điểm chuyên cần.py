class ClassName(object):
	def __init__(self, msv,name,lop):
		self.msv=msv
		self.name=name
		self.lop=lop
t=int(input())
n=t
list=[]
i=0
while i<t:
	list.append(ClassName(input(),input(),input()))
	i+=1
while(n>0):
	n-=1
	a,b=[str(i) for i in input().split()]
	dem=10
	for i in b:
		if i=='v':
			dem-=2
		if i=='m':
			dem-=1
		if dem<0:
			dem=0
	for i in list:
		if(i.msv==a):
			i.cc=dem
			if dem==0:
				i.cdk='KDDK'
			else:
				i.cdk=''
for i in list:
	print(i.msv,i.name,i.lop,i.cc,i.cdk)
