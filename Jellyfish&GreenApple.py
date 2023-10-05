from math import gcd
for _ in range(int(input())):
    n, m = map(int, input().split())
    n %= m
    p = str(bin((m//gcd(n, m))))

    if p.count('1') > 1:
        print(-1)
    else:
        ans = 0
        while n:
            ans += n
            n *= 2
            n %= m
        print(ans)