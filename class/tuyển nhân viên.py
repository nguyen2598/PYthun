class NV():
	def __init__(self,so,ten,x,y):
		while x>10:
			x=x/10
		while y>10:
			y/=10
		self.so="TS"+str(so//10)+str(so%10)
		self.ten=ten.title()
		self.x=x
		self.y=y
		self.diem='%.2f' %((self.x+self.y)/2)
		if float(self.diem)<5:
			self.TT='TRUOT'
		elif float(self.diem)<8:
			self.TT='CAN NHAC'
		elif float(self.diem)<=9.5:
			self.TT='DAT'
		else:
			self.TT='XUAT SAC'
	def __str__(self):
		return "{} {} {} {}".format(self.so,self.ten,self.diem,self.TT)
t=int(input())
j=1
list=[]
while t>0:
	t-=1
	a=NV(j,input(),float(input()),float(input()))
	j+=1
	list.append(a)
list.sort(key=lambda x: x.diem, reverse=True)
for i in list:
    print(i)