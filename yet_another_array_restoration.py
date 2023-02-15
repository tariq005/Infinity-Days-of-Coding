for _ in range(int(input())):
    n, x, y= map(int, input().split())
    p= y-x
    d= p//n
    a= [(x+i*d) for i in range(n)]

    while y not in a:
        d += 1
        while p%d:
            d += 1
        a= [x+(i*d) for i in range(n)]

    r= x%d
    while 1:
        a= [r+(i*d) for i in range(n)]
        r += d
        if x in a and y in a and 0 not in a:
            break

    print(*a)