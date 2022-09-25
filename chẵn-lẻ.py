def check(n):
    s = str(n)
    tong = 0
    for i in s: tong += int(i)
    if (tong % 10 == 0): return True
    return False


def check1(n):
    s = str(n)
    for i in range(len(s) - 1):
        if abs(int(s[i]) - int(s[i + 1])) != 2:
            return False
    return True


t = int(input())
while t:
    s = int(input())
    if check(s) and check1(s):
        print("YES")
    else:
        print("NO")
    t-=1