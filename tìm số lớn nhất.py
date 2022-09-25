def convert(s,n):
    if n==2:
        return s
    ans = 0
    k = len(s)-1
    for i in range(len(s)-1,-1,-1):
        ans = ans + int(s[i])*(2**(k-i))
    if n==10:
        return ans
    if n==16:
        return hex(ans).upper()[2:]
    if n==8:
        return oct(ans)[2:]
T=int(input())
for t in range(T):
    n = int(input())
    s = input()
    print(convert(s,n))