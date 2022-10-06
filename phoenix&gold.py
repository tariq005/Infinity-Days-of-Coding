for i in range(int(input())):
    n, x= map(int, input().split())
    w= list(map(int, input().split()))

    if sum(w) == x:
        print('NO')
    else:
        print('YES')
        j= 0
        s= 0

        while j<n:
            s += w[j]
            if s == x:
                w[j], w[j+1]= w[j+1], w[j]
                break
            j += 1

        print(*w)