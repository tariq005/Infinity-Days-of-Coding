import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    dis = [0]*n
    dis[0], dis[n-1] = 2, n-1
    for i in range(1, n-1):
        if a[i+1]-a[i] < a[i]-a[i-1]:
            dis[i] = i+2
        else:
            dis[i] = i

    prefix = [0]*(n+1)
    suffix = [0]*(n+1)
    prefix[0], suffix[n] = 0, 0
    for i in range(1, n):
        if dis[i-1] == i+1:
            prefix[i] = prefix[i-1]+1
        else:
            prefix[i] = prefix[i-1]+abs(a[i]-a[i-1])
        if dis[n-i] == n-i:
            suffix[n-i] = suffix[n-i+1]+1
        else:
            suffix[n-i] = suffix[n-i+1]+abs(a[n-i]-a[n-i-1])

    for i in range(int(input())):
        x, y = map(int, input().split())
        if x < y:
            print(prefix[y-1]-prefix[x-1])
        else:
            print(suffix[y]-suffix[x])
