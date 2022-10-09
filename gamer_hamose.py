import sys
input = sys.stdin.readline

for i in range(int(input())):
    a, b = map(int, input().split())
    l = list(map(int, input().split()))
    l.sort(reverse=True)
    cnt = 0
    add = l[0] + l[1]
    cnt = b // add
    cnt = cnt * 2
    if b % add == 0:
        print(cnt)
    elif b % add > l[0]:
        print(cnt + 2)
    else:
        print(cnt + 1)
