for _ in range(int(input())):
    n= int(input())
    a= list(map(int, input().split()))

    if len(set(a)) == 1:
        print('YES')
    else:
        l= 0
        r= 0
        valley= 0
        for i in range(1, n):
            if a[l] == a[i]:
                r= i
            else:
                if (l == 0 or a[l-1] > a[l]) and (r == n-1 or a[r] < a[r+1]):
                    valley += 1
                l= i
                r= l
        if a[l-1] > a[l]:
            valley += 1

        if valley == 1:
            print('YES')
        else:
            print('NO')