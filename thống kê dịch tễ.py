
a=[]

n,m=[int(i)for i in input().split()]
k=[]
def Try(i,j):
	dem=0
	k[i][j]=False
	if i>0 and a[i-1][j]!=-1 and k[i-1][j]:
		dem+=1
		k[i-1][j]=False
	if i>0 and j<m-1 and a[i-1][j+1]!=-1 and k[i-1][j+1]:
		dem+=1
		k[i-1][j+1]=False
	if j<m-1 and a[i][j+1]!=-1 and k[i][j+1]:
		dem+=1
		k[i][j+1]=False
	if i<n-1 and j<m-1 and a[i+1][j+1]!=-1 and k[i+1][j+1]:
		dem+=1
		k[i+1][j+1]=False
	if i<n-1 and a[i+1][j]!=-1 and k[i+1][j]:
		dem+=1
		k[i+1][j]=False
	if i<n-1 and j>0 and a[i+1][j-1]!=-1 and k[i+1][j-1]:
		dem+=1
		k[i+1][j-1]=False
	if j>0 and a[i][j-1]!=-1 and k[i][j-1]:
		dem+=1
		k[i][j-1]=False
	if i>0 and j>0 and a[i-1][j-1]!=-1 and k[i-1][j-1]:
		dem+=1
		k[i-1][j-1]=False
	return dem
dem=0

for i in range(n):
	a.append([int(i)for i in input().split()])
	b=[]
	for j in range(m):
		b.append(True)
	k.append(b)
for i in range(n):
	for j in range(m):
		if a[i][j]==-1:
			dem+=Try(i,j)
print(dem)