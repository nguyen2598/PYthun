t=int(input())
while t>0:
    t-=1
    kt=0
    s=input()
    for i in range(0,len(s)):
        if s[i]<='9' and s[i]>='0':
            for j in range(int(s[i])):
                if i>0:print(s[i-1],end='')
    print("")