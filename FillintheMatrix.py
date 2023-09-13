for _ in range(int(input())):
    n, m = map(int, input().split())
    if m == 1:
        print(0)
    elif n == 1:
        print(2)
    elif n >= m:
        print(m)
    else:
        print(n+1)

    if n >= m:
        p = n-m+2
        k = 0
        a = [[] for i in range(n)]
        for i in range(n):
            if p > 0:
                for j in range(m):
                    a[i] += [(j+k) % m]
                p -= 1
                i += 1
            else:
                k += 1
                for j in range(m):
                    a[i] += [(j+k) % m]
                i += 1

        for x in a:
            print(*x)
    else:
        k = 0
        a = [[] for i in range(n)]
        for i in range(n):
            for j in range(m):
                a[i] += [(j + k) % m]
            i += 1
            k += 1
        for x in a:
            print(*x)
