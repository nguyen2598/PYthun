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
	def __init__(self,dem,name,soP,vao,ra,tien):
		self.ma='KH'+str(dem//10)+str(dem%10)
		self.name=name
		self.soP=soP
		if soP//100==1:
			self.tin=25
		elif soP//100==2:
			self.tin=34
		elif soP//100==3:
			self.tin=50
		else:
			self.tin=80
		self.soN=NgayO(ra,vao)+1
		# print(self.soN)
		self.tie=(self.tin)*(self.soN)+tien
	def __str__(self):
		return "{} {} {} {} {}".format(self.ma, self.name, self.soP,self.soN,self.tie)
list=[]
t=int(input())
i=1
while t>0:
	t-=1
	list.append(hoadon(i,input(),int(input()),input(),input(),int(input())))
	i+=1
list.sort(key=lambda x: x.tie, reverse=True)
for i in list:
	print(i)