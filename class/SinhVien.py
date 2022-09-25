class SinhVien():
	def __init__(self , name,date,x,y,z):
		self.name=name
		self.date=date
		self.x=x
		self.y=y
		self.z=z
	def out(self):
		print(self.name,self.date,self.x+self.y+self.z)
s=input()
dt=input()
xx=float(input())
xy=float(input())
xz=float(input())
a= SinhVien(s,dt,xx,xy,xz)
a.out()