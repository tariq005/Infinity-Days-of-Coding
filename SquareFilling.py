n, m= map(int, input().split())
a= []
for _ in range(n):
    b= list(map(int, input().split()))
    a.append(b)

c= []
for i in range(n-1):
    for j in range(m-1):
        if a[i][j]* a[i][j+1]* a[i+1][j]* a[i+1][j+1] >0:
            a[i][j]= 2
            a[i+1][j]= 2
            a[i][j+1]= 2
            a[i+1][j+1]= 2
            c.append((i+1, j+1))

count= 0
for i in range(n):
    for j in range(m):
        if a[i][j] == 1:
            count += 1

if count>0:
    print(-1)
else:
    print(len(c))
    for x in c:
        print(*x)