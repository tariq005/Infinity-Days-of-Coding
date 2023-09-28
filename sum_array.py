for _ in range(int(input())):
    n, k = map(int, input().split())
    m = n//2
    
    if m%2 == k%2:
        if m*3 <= k:
            a = [1]*m + [2]*m
            r = k- 3*m
            p = 100000-2
            for i in range(n):
                if r == 0:
                    break
                a[i] += min(r, p)
                r -= min(r, p)
            if r == 0:
                print(*a)
            else:
                print(-1)
        else:
            print(-1)
    else:
        print(-1)
