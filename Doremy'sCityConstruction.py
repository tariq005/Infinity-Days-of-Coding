for _ in range(int(input())):
    n= int(input())
    a= list(map(int, input().split()))
    a.sort()
    edges= n//2

    for i in range(1, n):
        if a[i] != a[i-1]:
            edges= max(edges, i*(n-i))
    print(edges)
    