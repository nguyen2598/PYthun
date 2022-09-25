t = int(input())
for c in range(t):
    kt="YES"
    s=input().split('.')
    if(len(s)!=4):
        kt="NO"
    else:
        for i in s:
            if i.isdigit()==False or int(i)>255:
                kt="NO"
                break
    print(kt)