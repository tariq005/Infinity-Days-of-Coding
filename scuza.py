for i in range(int(input())):
    n, q= map(int, input().split())
    a= list(map(int, input().split()))
    k= list(map(int, input().split()))

    c= list(range(q))
    d= [x for _,x in sorted(zip(k, c))]
    e= [0]*q

    m= 0
    s= 0
    for j in d:
        while m<n:
            if a[m] <= k[j]:
                s += a[m]
                m += 1
            else:
                break
        e[j]= s

    print(*e)