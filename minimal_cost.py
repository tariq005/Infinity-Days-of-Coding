import math
for _ in range(int(input())):
    n, u, v= map(int, input().split())
    a= list(map(int, input().split()))
    ans= math.inf

    for i in range(n-1):
        diff= abs(a[i+1]-a[i])
        if diff > 1:
            ans= 0
        if diff == 1:
            ans= min(ans, min(u, v))
        else:
            ans= min(ans, v+min(u, v))
    print(ans)