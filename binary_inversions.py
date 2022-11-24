for _ in range(int(input())):
    n= int(input())
    a= list(map(int, input().split()))
    u= 0
    v= 0
    w= 0
    p= 0

    for i in range(n):
        if a[i] == 1:
            p += 1
        else:
            u += p

    if 0 in a:
        p= 0
        for i in range(n):
            if a[i] == 0:
                a[i]= 1
                break

        for j in range(n):
            if a[j] == 1:
                p += 1
            else:
                v += p
        a[i]= 0

    if 1 in a:
        p= 0
        for i in range(n-1, -1, -1):
            if a[i] == 1:
                a[i]= 0
                break

        for k in range(n):
            if a[k] == 1:
                p += 1
            else:
                w += p
        a[i]= 1

    print(max(u, v, w))