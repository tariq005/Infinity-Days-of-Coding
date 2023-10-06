for _ in range(int(input())):
    n, s1, s2 = map(int, input().split())
    r = list(map(int, input().split()))
    c = list(range(1, n+1))
    z = [x for _, x in sorted(zip(r, c))][::-1]
    a, b = [], []
    i, j, k = 1, 1, 0

    while k < n:
        if s1*i < s2*j:
            a.append(z[k])
            i += 1
        else:
            b.append(z[k])
            j += 1
        k += 1

    print(len(a), *a)
    print(len(b), *b)
