from collections import defaultdict
for _ in range(int(input())):
    x, y, k1, k2 = defaultdict(int), defaultdict(int), defaultdict(int), defaultdict(int)
    for i in range(int(input())):
        x1, y1 = map(int, input().split())
        x[str(x1)] += 1
        y[str(y1)] += 1
        k1[str(y1-x1)] += 1
        k2[str(y1+x1)] += 1

    ans = 0
    for i in x:
        ans += x[i] * (x[i]-1)
    for i in y:
        ans += y[i] * (y[i]-1)
    for i in k1:
        ans += k1[i] * (k1[i]-1)
    for i in k2:
        ans += k2[i] * (k2[i]-1)
    print(ans)
