t = int(input())
while t>0:
    s = input()
    dem = 0
    for i in s:
        if i == '4' or i == '7':
            dem += 1
    if dem==len(s) :
        print("YES")
    else : print("NO")
    t-=1