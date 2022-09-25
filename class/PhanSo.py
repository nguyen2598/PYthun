import math
class PhanSo(object):
	def __init__(self,x,y):
		self.x=x
		self.y=y
	def phanso(self,q):
		xx=self.x*q.y+self.y*q.x
		yy=self.y*q.y
		gcd=(math.gcd(xx,yy))
		print("{}/{}".format(int(xx/ gcd),int(yy / gcd)))	
n,m,c,d=[int(i) for i in input().split()]
a=PhanSo(n,m)
b=PhanSo(c,d)
a.phanso(b)
