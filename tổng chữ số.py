s = input()
buoc = 0
while len(s) > 1:
    sum = 0
    for i in range(0,len(s)):
        sum+= (ord(s[i])-48)
    s = str(sum)
    buoc+=1
print(buoc)