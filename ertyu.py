n=int(input())
k = list(map(int,input().split()))
z=[]
t=[]
for i in range(len(k)): 
    if k[i]%2==0:
        z.append(k[i])
    elif k[i]%2==1:
        t.append(k[i])
print(*t)
print(*z)
if len(z)>=len(t): 
	print('YES') 
else: 
    print('NO')