for _ in range(int(input())):
    n= int(input())
    a= list(map(int, input().split()))
    
    if n == 1:
        print(0)
    else:
        m= len(set(a))
        if m == n:
            print(-1)
        else:
            d= {}
            for x in a:
                if x in d:
                    d[x] += 1
                else:
                    d[x]= 1
            p= max(d.values())
            if p == n:
                print(0)
            else:
                print(n-p+1)
