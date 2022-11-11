import sys
input= sys.stdin.readline
for _ in range(int(input())):
    n= int(input())
    d= {}
    for i in map(int, input().split()):
        if i in d:
            d[i] += 1
        else:
            d[i]= 1
    if n<3:
        print(0)
    else:
        print(n-max(2, max(d.values())))
