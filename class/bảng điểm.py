from decimal import Decimal


def xet(n):
    if n >= 108:
        return 'XUAT SAC'
    elif n >= 96:
        return 'GIOI'
    elif n >= 84:
        return 'KHA'
    elif n >= 60:
        return 'TB'
    else:
        return 'YEU'


class Diem(object):

    def __init__(self, ten, arg, ma):
        self.ten = ten
        self.tongdiem = sum(arg)
        self.diem = round((self.tongdiem / 10/1.2), 1)
        # self.msv = 'HS' + maso(ma)
        if ma < 10:
            self.msv = "HS0" + str(ma)
        else:
            self.msv = "HS" + str(ma)
        self.xeploai = xet(self.tongdiem)


t = int(input())
stt = 1
lstsv = []
while stt <= t:
    ten = input()
    lstdiem = [(float(x)) for x in input().split()]
    lstdiem.extend([lstdiem[0], lstdiem[1]])
    lstsv.append(Diem(ten, lstdiem, stt))
    stt += 1
lstsv.sort(key=lambda CD: (CD.tongdiem), reverse=True)
for i in lstsv:
    print('{} {} {} {}'.format(i.msv, i.ten, i.diem, i.xeploai))
