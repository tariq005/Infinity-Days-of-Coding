for _ in range(int(input())):
    n = int(input())
    a = sorted([(b, i)for i, b in enumerate(map(int, input().split()))])
    ans = [0]*n
    s1 = 0
    s2 = sum(a[i][0] for i in range(n))

    for i in range(n):
        ans[a[i][1]] = s2+n+a[i][0]*(2*i-n)-s1
        s1 += a[i][0]
        s2 -= a[i][0]
    print(*ans)
