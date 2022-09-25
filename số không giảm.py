t=int(input())
while t>0:
    t-=1
    kt=0
    s=input()
    for i in range(1,len(s)):
        if s[i]<s[i-1]:
            kt=1
            break
    if kt==0:
        print("YES")
    else:
        print("NO")
