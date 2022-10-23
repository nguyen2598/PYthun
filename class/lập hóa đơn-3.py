import datetime
def NgayO(ra,vao):
	a,b,c=[int(i) for i in ra.split('/')]
	x = datetime.datetime(c, b, a)
	a,b,c=[int(i) for i in vao.split('/')]
	y = datetime.datetime(c, b, a)
	xx=str(x-y).split()
	if(len(xx)>1):
		return int(xx[0])
	else :
		return 0
class hoadon():
	def __init__(self,dem,name,soP,vao,ra):
		self.ma=dem
		self.name=name
		self.soP=soP
		self.vao=vao
		self.ra=ra
		self.tien=vao*soP-ra
	def __str__(self):
		return "{} {} {} {} {} {}".format(self.ma, self.name,self.soP, self.vao,self.ra,self.tien)
list=[]
t=int(input())
i=1
while t>0:
	t-=1
	list.append(hoadon(input(),input(),int(input()),int(input()),int(input())))
	i+=1
list.sort(key=lambda x: x.tien, reverse=True)
for i in list:
	print(i)