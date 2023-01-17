import sys
input= sys.stdin.readline
for _ in range(int(input())):
    n= int(input())
    a= list(map(int, input().split()))
    a.sort()
    way= 0

    if 0 not in a:
        way += 1

    for i in range(n):
        if a[i] < i+1 and (i == n-1 or a[i+1]>i+1):
            way += 1

    print(way)