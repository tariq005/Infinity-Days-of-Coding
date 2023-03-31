for _ in range(int(input())):
    n, m= map(int, input().split())
    a= []
    for i in range(n):
        b= list(map(int, input().split()))
        for j in b:
            a.append([j, i])
    a.sort()

    jogging= [[-1 for i in range(m)] for j in range(n)]
    for i in range(m):
        jogging[a[i][1]][i]= a[i][0]
    for j in range(m, n*m):
        k= 0
        while jogging[a[j][1]][k] != -1:
            k += 1
        jogging[a[j][1]][k]= a[j][0]

    for x in jogging:
        print(*x)