from math import gcd
for _ in range(int(input())):
    n= int(input())
    a= list(map(int, input().split()))
    b= []

    for i in range(n//2):
        b.append(abs(a[i]-a[n-i-1]))
    g= 0
    for x in b:
        g= gcd(g, x)
    print(g)
