from math import gcd
for _ in range(int(input())):
    a, b= map(int, input().split())
    while gcd(a, b)>1:
        b //= gcd(a, b)
    if b == 1:
        print('YES')
    else:
        print('NO')
