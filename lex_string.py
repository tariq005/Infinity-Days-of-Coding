for _ in range(int(input())):
    n, m, k= map(int, input().split())
    a= input()
    b= input()
    a, b= sorted(a), sorted(b)
    s= str()
    i, j, count_a, count_b= 0, 0, 0, 0

    while i<n and j<m:
        if a[i] <= b[j]:
            if count_a<k:
                s += a[i]
                count_a += 1
                count_b= 0
                i += 1
            else:
                s += b[j]
                count_a= 0
                count_b += 1
                j += 1
        else:
            if count_b<k:
                s += b[j]
                count_b += 1
                count_a= 0
                j += 1
            else:
                s += a[i]
                count_a += 1
                count_b= 0
                i += 1

    print(s)