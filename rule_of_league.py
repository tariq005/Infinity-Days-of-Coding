import sys
input= sys.stdin.readline
for _ in range(int(input())):
    n, x, y= map(int, input().split())
    p= max(x, y)

    if min(x,y) != 0:
        print(-1)
    elif p == 0 or (n - 1) % p != 0:
        print(-1)
    else:
        ans= []
        for i in range(2, n+1, p):
            ans += [i]*p

        print(*ans)