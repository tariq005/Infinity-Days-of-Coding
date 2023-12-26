for _ in range(int(input())):
    n, k, d = map(int, input().split())
    a = list(map(int, input().split()))
    v = list(map(int, input().split()))
    ans = 0

    for i in range(min(d, 2*n)):
        count = 0
        for j in range(n):
            count += a[j] == j+1
        count += (d-i-1)//2
        ans = max(count, ans)
        for x in range(v[i%k]):
            a[x] += 1
    print(ans)
