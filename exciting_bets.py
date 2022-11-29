for _ in range(int(input())):
    a, b= map(int, input().split())

    if a == b:
        print(0, 0)
    else:
        d= abs(a-b)
        f= max(a, b)%d
        print(d, min(d-f, f))