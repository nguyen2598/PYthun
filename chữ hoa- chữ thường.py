s = input()
d = {thuong: 0, hoa: 0}
for i in s:
    if i.isupper(): d.hoa += 1
    if i.islower(): d.thuong += 1
if d.thuong >= d.hoa:
    print(s.lower())
else:
    print(s.upper())
