n, k= map(int, input().split())
a= list(map(int, input().split()))
a.sort()
ans= 0

if k == 0:
    ans= a[0]-1
else:
    ans= a[k-1]

count= 0
for x in a:
    if x <= ans:
        count += 1

if ans<1 or count != k:
    print(-1)
else:
    print(ans)