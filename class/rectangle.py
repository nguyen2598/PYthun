def replaCe(s):
    s=s.title()
    return s
class Rectangle():
    def __init__(self,x1,x2,x3):
        self.x1=x1
        self.x2=x2
        self.x3=replaCe(x3)
    def perimeter(self):
        return (self.x1+self.x2)*2
    def area(self):
        return self.x2*self.x1
    def color(self):
        return self.x3
arr = input().split()
if int(arr[0])<=0 or int(arr[1])<=0:
    print('INVALID')
else:         
    r = Rectangle(int(arr[0]), int(arr[1]), str(arr[2]))
    print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))
