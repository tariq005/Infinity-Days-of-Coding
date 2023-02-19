from collections import Counter

for _ in range(int(input())):
    N = int(input())
    arr = list(map(int, input().split()))
    ans = 0
    c = Counter(i.bit_length() for i in arr)

    for k, v in c.items():
        if (v > 1):
            ans += (v * (v - 1) // 2)
    print(ans)