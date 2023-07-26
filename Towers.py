from bisect import bisect_right
n = int(input())
a = list(map(int, input().split()))
b = []
ans = 0

for i in a:
    pos = bisect_right(b, i)
    if pos >= ans:
        b += [i]
        ans += 1
    else:
        b[pos] = i

print(ans)
