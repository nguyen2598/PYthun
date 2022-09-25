T = int(input())
for t in range(T):
    n = input()
    m=input()
    dem=0
    n=n.replace(m,'$')
    dem=n.count('$')
    print(dem)