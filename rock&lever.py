from collections import Counter

for _ in range(int(input())):
    n= int(input())
    a= list(map(int, input().split()))
    ans = 0
    c= Counter(x.bit_length() for x in a)

    for k, v in c.items():
        ans += (v * (v - 1) // 2)
    print(ans)
