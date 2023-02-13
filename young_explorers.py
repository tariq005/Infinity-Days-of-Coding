import sys
input= sys.stdin.readline
for _ in range(int(input())):
    n= int(input())
    e= list(map(int, input().split()))
    c= sorted(e, reverse= True)
    explorers= 0
    count= 0
    while c:
        count += 1
        if count >= c.pop():
            explorers += 1
            count= 0
    print(explorers)