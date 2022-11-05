for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    m = min(a)

    if m in a[1:] and a[0] != m:
        print('Alice')
    else:
        print('Bob')
