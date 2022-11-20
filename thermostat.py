for _ in range(int(input())):
    l, r, x= map(int, input().split())
    a, b= map(int, input().split())

    if a == b:
        print(0)
    elif abs(a-b) >= x:
        print(1)
    elif b>a:
        if b+x <= r or a-x >= l:
            print(2)
        elif a+x <= r and b-l >= x:
            print(3)
        else:
            print(-1)
    elif b<a:
        if b-x >= l or a+x <= r:
            print(2)
        elif b+x <= r and a-l >= x:
            print(3)
        else:
            print(-1)