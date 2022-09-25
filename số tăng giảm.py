def kt(n):
    if len(n)<3: return "NO"
    # if n[0]>n[1]: return "NO"
    ok = True
    for i in range(1,len(n)-1):
        if n[i-1]<n[i]>n[i+1]: ok = False
        if ok:
            if n[i]>=n[i+1]: return "NO"
        else:
            if n[i]<=n[i+1]: return "NO"
    return "YES"
t = int(input())
for e in range(t):
    s = input()
    print(kt(s))