t = int(input())
while t:

    s = str(input())
    if s[0] == s[len(s) - 2] and s[1] == s[len(s) - 1]:
        print("YES")
    else:
        print("NO")
    t -= 1
