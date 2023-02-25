for _ in range(int(input())):
    n, h= map(int, input().split())
    a= list(map(int, input().split()))
    a.sort()
    l, r= 1, h

    while l<r:
        mid= (l+r)//2
        damage= sum([min(mid, a[i+1]-a[i]) for i in range(n-1)]+ [mid])
        if damage >= h:
            r= mid
        else:
            l= mid+1
    print(l)