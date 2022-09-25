Prime = [True]*1000006
for i in range(2,1000001):
    if Prime[i]:
        for j in range(2*i,1000001,i):
            Prime[j]=False
def Do(n):
        check = [False]*1000006
        N = int(n)
        for i in range(13,N):
            j = int(str(i)[::-1])
            if i>=N or j>=N: continue
            if not check[i]:
                if not check[j]:
                    if i!=j:
                        if Prime[i]:
                            if Prime[j]:
                                check[i]=True
                                check[j]=True
                                print(i,j,end=" ")
        return 0
T = int(input())
for t in range(T):
    n = input()
    Do(n)
    print()