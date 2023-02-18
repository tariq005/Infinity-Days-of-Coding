for _ in range(int(input())):
    n, k= map(int, input().split())
    r= n%3

    if r == 0:
        print(n//3, n//3, n//3)
    else:
        if n%2:
            n -= 1
            print(1, n//2, n//2)
        else:
            if n%4:
                n -= 2
                print(2, n//2, n//2)
            else:
                p= n//2
                print(p, p//2, p//2)