for _ in range(int(input())):
    n, k = map(int, input().split())

    if n % 2 == 0:
        if k % n == 0:
            print(n)
        else:
            print(k % n)
    else:
        print(1 + (k-1 + ((k-1) // ((n-1)//2))) % n)
