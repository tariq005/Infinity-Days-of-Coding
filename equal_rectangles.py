for _ in range(int(input())):
    n= int(input())
    a= list(map(int, input().split()))
    a.sort()
    area= a[0]*a[4*n-1]
    i= 0

    while i<2*n:
        if a[2*i] == a[2*i+1] and a[4*n-2*i-1] == a[4*n-2*i-2] and area == a[2*i]*a[4*n-2*i-1]:
            i += 2
        else:
            print('NO')
            break
    else:
        print('YES')