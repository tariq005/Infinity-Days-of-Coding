for _ in range(int(input())):
    n, m= map(int, input().split())
    p= pow(pow(2, n, 1000000007) -1, m, 1000000007)
    print(p)
