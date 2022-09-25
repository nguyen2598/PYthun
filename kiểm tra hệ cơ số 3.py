t=int(input())
while t>0:
    t-=1
    s=str(input())
    ok=False
    for i in s:
        if(i!='0' and i!='1' and i!='2' ):
            ok=True
    if(ok):
        print('NO')
    else:
        print('YES')