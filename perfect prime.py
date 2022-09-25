import math

def nto(a):
    for i in range(2, int(math.sqrt(a)+1)):
        if a % i == 0: return 1
    return 0
t = int(input())
while t > 0:
    t-=1
    s = int(input())
    if(nto(s) == 1): 
        print("NO")
    else:
        print("YES")