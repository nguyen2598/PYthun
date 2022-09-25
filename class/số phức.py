class soPhuc():
	def __init__(self,x1,y1,x2,y2):
		self.x1=x1
		self.y1=y1
		self.x2=x2
		self.y2=y2
	def A_B(self):
		x=(self.x1+self.x2)*self.x1-(self.y1+self.y2)*self.y1
		y=(self.x1+self.x2)*self.y1+(self.y1+self.y2)*self.x1
		print(x,end=' ')
		if y>=0:
			print('+',y,end='i, ')
		else:
			print('-',-y,end='i, ')
	def A_B_A(self):
		x=(self.x1+self.x2)*(self.x1+self.x2)-(self.y1+self.y2)*(self.y1+self.y2)
		y=2*(self.x1+self.x2)*(self.y1+self.y2)
		print(x,end=' ')
		if y>=0:
			print('+',y,end='i ')
		else:
			print('-',-y,end='i ')
t=int(input())
while t>0:
	t-=1
	a,b,c,d=[int(i) for i in input().split()]
	r=soPhuc(a,b,c,d)
	r.A_B()
	r.A_B_A()
	print('')