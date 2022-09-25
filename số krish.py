def Fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*Fact(n-1)
def Krish(n):
    intN = int(n)
    sum = 0
    for i in n:
        sum += Fact(int(i))
    if sum == intN:
        return "Yes"
    return "No"
T=int(input())
for t in range(T):
    n = input()
    print(Krish(n))