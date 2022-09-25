def prime(n):
    if n < 2: return 0
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0: return 0
    return 1


t = int(input())
while t:
    s = int(input())
    a = str(s)
    tong = 0;
    for i in a:
        tong += int(i)
    if (prime(tong)):
        print("YES")
    else:
        print("NO")
    t-=1
