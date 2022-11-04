for _ in range(int(input())):
    n, k, r, c= map(int, input().split())
    a= [['.' for x in range(n)] for y in range(n)]
    for i in range(n):
        for j in range(n):
            b= (c+r)- (i+j+2)
            if b%k == 0:
                a[i][j]= 'X'
            else:
                continue
    for k in range(n):
        print(*a[k], sep='')