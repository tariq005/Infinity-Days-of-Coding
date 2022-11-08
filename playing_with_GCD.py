from math import  *
import sys
input= sys.stdin.readline
for _ in range(int(input())):
    n= int(input())
    a= list(map(int, input().split()))
    ans= 'YES'

    b= [a[0]]
    for i in range(1, n):
        b.append(lcm(a[i], a[i-1]))
    b.append(a[n-1])
    for j in range(n):
        if gcd(b[j], b[j+1]) != a[j]:
            ans= 'NO'

    print(ans)