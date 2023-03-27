for _ in range(int(input())):
    n, m, k= map(int, input().split())
    h= list(map(int, input().split()))

    for i in range(1, n):
        m += h[i-1]- max(0, h[i]-k)
        if m<0:
            print('NO')
            break
    else:
        print('YES')