for _ in range(int(input())):
    n= int(input())
    a= list(map(int, input().split()))

    multi= 0
    for x in a:
        while x%2 == 0:
            multi += 1
            x //= 2

    if multi >= n:
        print(0)
    else:
        b= list(range(n+1))
        i= 1
        while i<n+1:
            j= i
            count= 0
            while j%2 == 0:
                count += 1
                j //= 2
            b[i]= count
            i += 1

        b= sorted(b, reverse=True)
        res= 0
        for x in b:
            multi += x
            res += 1
            if multi >= n:
                break
        print(res if multi >= n else -1)