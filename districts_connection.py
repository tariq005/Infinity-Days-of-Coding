for _ in range(int(input())):
    n= int(input())
    a= list(map(int, input().split()))

    if len(set(a)) == 1:
        print('NO')
    elif len(set(a)) == n:
        print('YES')
        for i in range(1, n):
            print(1, i+1)
    else:
        print('YES')
        p= a[0]
        r= []
        q= 0
        for i in range(1, n):
            if p == a[i]:
                r.append(i+1)
            else:
                print(1, i+1)
                q= i+1
        for x in r:
            print(q, x)