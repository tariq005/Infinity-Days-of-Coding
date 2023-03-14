import sys
input= sys.stdin.readline
for _ in range(int(input())):
    n, x= map(int, input().split())
    a= list(map(int, input().split()))

    if n >= 2*x:
        print('YES')
    else:
        b= sorted(a)
        for i in range(n-x, x, 1):
            if a[i] != b[i]:
                print('NO')
                break
        else:
            print('YES')