for _ in range(int(input())):
    n, k = map(int, input().split())

    if n > k:
        a = (((n%k)//2)%k)*((n-((n%k)//2))%k)
        b = (((k+n%k)//2)%k)*((n-(k+n%k)//2)%k)
        if a > b:
            print((n%k)//2)
        else:
            print((k+n%k)//2)
    else:
        print(n//2)
