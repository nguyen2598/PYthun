T = int(input())-1
s=input()
Set={s}
for i in range(T):
	s=input()
	Set.add(s)
print(len(Set))
