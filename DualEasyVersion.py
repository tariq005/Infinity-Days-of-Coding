for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    if sorted(a) == a:
        print(0)
    else:
        b = []
        if abs(max(a)) < abs(min(a)):
            j = a.index(min(a))
            for i in range(n-2, -1, -1):
                while a[i] > a[i+1]:
                    a[i] += a[j]
                    b.append((i+1, j+1))
                    if a[i] < a[j]:
                        j = i
        else:
            j = a.index(max(a))
            for i in range(1, n):
                while a[i] < a[i-1]:
                    a[i] += a[j]
                    b.append((i+1, j+1))
                    if a[i] > a[j]:
                        j = i

        print(len(b))
        for s in b:
            print(*s)
