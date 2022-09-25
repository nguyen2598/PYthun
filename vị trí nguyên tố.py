import math
def nt(n):
    if n<2 :return 0
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return 0
    return 1
def kt(s):
    for i in range(len(s)):
        if (nt(i)==1 and nt(int(s[i]))==0) or (nt(i)==0 and nt(int(s[i]))==1) :
            return "NO"
    return "YES"
T = int(input())
for t in range(T):
    n = input()
    print(kt(n))