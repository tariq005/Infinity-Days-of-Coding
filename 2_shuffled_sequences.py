import sys
input= sys.stdin.readline
n= int(input())
a= list(map(int, input().split()))
a.sort()
incr= a[::2]
decr= a[1::2]

if len(set(incr))+ len(set(decr)) < n:
    print('No')
else:
    decr= decr[::-1]
    print('Yes')
    print(len(incr))
    print(*incr)
    print(len(decr))
    print(*decr)