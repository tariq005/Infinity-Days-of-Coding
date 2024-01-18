for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = sorted(a)
    p = [0]*n
    p[0] = b[0]
    for i in range(n):
        p[i] = p[i-1] + b[i]

    d = dict()
    d[b[n-1]] = n-1
    for i in range(n-2, -1, -1):
        if p[i] >= b[i+1]:
            d[b[i]] = d[b[i+1]]
        else:
            d[b[i]] = i

    for i in range(n):
        print(d[a[i]], end=" ")
    print()
