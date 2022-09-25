import math
t=int(input())
while t>0:
    t-=1
    kt=0
    s=int(input())
    print('1 * ',end='')
    for i in range(2,int(math.sqrt(s))+1):
        dem=0
        if s%i==0:
            while s%i==0:
                dem+=1
                s//=i
            print(i,end='^')
            print(dem,end=' ')
            if s>1:
                print('',end='* ')
    if s>1:
        print(s,end='^1')
    print('')
