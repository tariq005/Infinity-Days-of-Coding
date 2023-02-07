for _ in range(int(input())):
    n= int(input())
    w= list(map(int, input().split()))
    pos= {}

    for x in w:
        if x in pos:
            pos[x] += 1
        else:
            pos[x]= 1

    maxx= 0
    s= 2
    while s <= 2*n:
        total= 0
        for x in pos:
            p= s-x
            if p>0 and p in pos:
                total += min(pos[x], pos[p])
        total //= 2
        maxx= max(total, maxx)
        s += 1

    print(maxx)
