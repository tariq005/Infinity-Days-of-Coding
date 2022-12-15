for _ in range(int(input())):
    n= int(input())
    a= list(map(int, input().split()))

    if n == 1:
        print(0)
    else:
        maxx= a[n-1]- a[0]
        for i in range(1, n):
            r= a[i-1]- a[i]
            maxx= max(maxx, r)
        t= max(max(a[1:])- a[0], a[n-1]- min(a[:n-1]))
        print(max(maxx, t))