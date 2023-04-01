import sys
input= sys.stdin.readline
for _ in range(int(input())):
    n= int(input())
    a= list(map(int, input().split()))
    s= set()

    for x in a:
        if x%5 == 0:
            s.add(x+ x%10)
            continue
        while x%10 != 6:
            x += x%10
        s.add(x%20)

    print('YES' if len(s) == 1 else 'NO')