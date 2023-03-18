for _ in range(int(input())):
    n= int(input())
    a= sorted(list(map(int, input().split())))
    b= sorted(list(map(int, input().split())))
    k= n-(n-(n//4))
    me= sum(a[k:])
    lily= sum(b[k:])
    count, i, j= 0, n//4, n//4

    while me < lily:
        me += 100
        count += 1
        if j and (n+count)%4:
            lily += b[j-1]
            j -= 1
        if not (n+count)%4:
            me -= a[i]
            i += 1
    print(count)