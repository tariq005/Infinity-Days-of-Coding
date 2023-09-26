for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(2, n):
        if a[i] > 0:
            ans += a[i]

    if n >= 2:
        if (a[0] <= 0) and (a[1] > 0):
            ans += max(a[1]+a[0], 0)
        else:
            for j in range(2):
                if a[j] > 0:
                    ans += a[j]
    else:
        if a[0] > 0:
            ans += a[0]
    print(ans)
