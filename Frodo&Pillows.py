n, m, k = map(int, input().split())
minimum = min(k - 1, n - k)
maximum = max(k - 1, n - k)
m -= n
result = 1
s = 1

for i in range(maximum + 1):
    if m - s < 0:
        break
    else:
        m -= s
        result += 1
        s += 2 if i < minimum else 1
else:
    result += m//n

print(result)
