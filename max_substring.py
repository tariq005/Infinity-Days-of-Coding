import sys
input= sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    s = input()
    a = s.count('1')
    m = a * (n-a)

    d = 1
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            d += 1
        else:
            m = max(m, d*d)
            d = 1

    m = max(m, d*d)
    print(m)