from builtins import object, int


def chiso(n):
    a = [0, 0, 0]
    if n <= 50:
        a[0] = n
    elif n <= 100:
        a[0] = 50
        a[1] = n - 50
    else:
        a[0] = 50
        a[1] = 50
        a[2] = n - 100
    return a


class HoaDon(object):
    def __init__(self, ma, ten, cu, moi):
        self.ten = ten
        self.cu = cu
        self.moi = moi
        if ma < 10:
            self.ma = "KH0" + str(ma)
        else:
            self.ma = "KH" + str(ma)
        self.m3 = moi - cu

    def tinh(self):
        a = chiso(self.m3)
        self.tong = 100 * a[0] + 150 * a[1] + 200 * a[2]
        if self.m3 <= 50:
            self.sum = round(self.tong + self.tong * 2 / 100)
        elif self.m3 <= 100:
            self.sum = round(self.tong + self.tong * 3 / 100)
        else:
            self.sum = round(self.tong + self.tong * 5 / 100)

    def __str__(self):
        return "{} {} {}".format(self.ma, self.ten, self.sum)


t = int(input())
list = []
for i in range(1, t + 1):
    a = HoaDon(i, input(), int(input()), int(input()))
    a.tinh()
    list.append(a)
list.sort(key=lambda x: x.sum, reverse=True)
for i in list:
    print(i)
