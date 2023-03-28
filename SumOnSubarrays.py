for _ in range(int(input())):
    n, k= map(int, input().split())

    if k == 0:
        a= [-1000]*n
        print(*a)
    elif k == (n*(n+1))//2:
        a= [1000]*n
        print(*a)
    elif n == k:
        a= [1000]
        for i in range(n-1):
            a.append(-1)
        print(*a)
    elif n>k:
        a= []
        for i in range(k-1):
            a.append(-1)
        a.append(abs(sum(a))+1)
        p= a[-1]*2
        for i in range(n-k):
            a.append(-p)
        print(*a)
    else:
        x= 1
        while (x*(x+1))//2 < k:
            x += 1
        if (x*(x+1))//2 != k:
            x -= 1
        r= k- (x*(x+1))//2
        a= []
        for i in range(x):
            a.append(2)
        q= sum(a)+1
        for j in range(r):
            q -= 2
        a.append(-q)
        m= n-len(a)
        for i in range(m):
            a.append(-1000)
        print(*a)