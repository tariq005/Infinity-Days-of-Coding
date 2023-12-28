for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    s = sum(a)
    
    if n == 1:
        if a[0] >= 2:
            print('Alice')
        else:
            print('Bob')
    elif s%2:
        print('Bob')
    else:
        p = sum(a[::2])
        print('Alice' if p%2 != (s//2)%2 else 'Bob')
