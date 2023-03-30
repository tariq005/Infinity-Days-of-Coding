import sys
input= sys.stdin.readline
for _ in range(int(input())):
    n, m= map(int, input().split())
    a= []
    for i in range(n):
        b= list(map(int, input().split()))
        a.append(b)

    casino= []
    for i in range(m):
        p= []
        for j in range(n):
            p.append(a[j][i])
        casino.append(sorted(p))

    ans= 0
    for x in casino:
        sum= []
        r= 0
        for i in range(n-1, 0, -1):
            r += x[i]
            sum.append(r)
        sum.sort()
        for j in range(n-1):
            ans += sum[j]- x[j]*(n-j-1)
    print(ans)