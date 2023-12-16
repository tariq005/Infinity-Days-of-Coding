for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    b.sort(reverse=True)
    c = []
    i, j = 0, 0

    while j < m:
        while j < m and b[j] >= a[i]:
            c.append(b[j])
            j += 1
        if j == m:
            break
        while i < n and b[j] < a[i]:
            c.append(a[i])
            i += 1
        if i == n:
            break

    if j == m:
        c += a[i:]
    if i == n:
        c += b[j:]
    print(*c)
