# from builtins import object, int
def Gio(s):
	a=s[0:2]
	b=s[3:5]
	return int(a)*60+int(b)
class Time():
	def __init__(self,ma,ten,vao,ra):
		self.ma=ma
		self.ten=ten
		self.gio=Gio(ra)-Gio(vao)
		self.time=str((Gio(ra)-Gio(vao))//60)+" gio "+str((Gio(ra)-Gio(vao))%60)+" phut"

	def __str__(self):
		return "{} {} {}".format(self.ma, self.ten, self.time)
t = int(input())
list = []
for i in range(1, t + 1):
    a = Time(input(), input(), input(), input())
    list.append(a)
list.sort(key=lambda x: x.gio, reverse=True)
for i in list:
    print(i)
