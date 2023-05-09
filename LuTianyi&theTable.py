for _ in range(int(input())):
    n, m = map(int, input().split())
    b = list(map(int, input().split()))
    b = sorted(b, reverse=True)

    diff = []
    for i in range(2):
        for j in range(-1, -3, -1):
            diff.append(b[i]-b[j])
    diff = sorted(diff, reverse=True)

    ans = 0
    p = (n*m)-1
    u = max(n, m)
    v = min(n, m)
    q = (u-1)*v
    ans += diff[0]*q
    ans += diff[1]*(p-q)
    print(ans)
