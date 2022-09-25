s=input().lower()
ss=input().lower()
SSet={''}
Set=(set(s.split()))
for i in ss.split():
	if i in Set:
		SSet.add(i)
for i in ss.split():
	Set.add(i)
print(" ".join(sorted(Set)))
print(" ".join(sorted(SSet)))
