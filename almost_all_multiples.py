for _ in range(int(input())):
    n, x= map(int, input().split())

    if n%x:
        print(-1)
    else:
        a= list(range(1, n+1))
        if x == n:
            a[0], a[-1]= a[-1], a[0]
            print(*a)
        else:
            a[0]= x
            b= [x]
            p= n//x
            for i in range(2, p+1):
                while p%i == 0:
                    p //= i
                    b.append(i*b[-1])
            a[-1]= 1
            for k in range(len(b)-1):
                a[b[k]-1]= b[k+1]
            print(*a)