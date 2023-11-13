for _ in range(int(input())):
    n, k = map(int, input().split())
    b = list(map(int, input().split()))

    if b[-1] > n:
        print('No')
    elif b[-1] == n:
        print('Yes')
    else:
        start = 0
        for i in range(min(n, k)):
            end = (start + n - 1) % n
            p = b[end]
            if p > n:
                print('No')
                break
            start = (start+n-p) % n
        else:
            print('Yes')
