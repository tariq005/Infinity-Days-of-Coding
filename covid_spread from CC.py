for i in range(int(input())):
    n, d= map(int, input().split())
    infected= [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 3072, 9216, 27648, 82944, 248832, 746496, 2239488, 6718464, 20155392, 60466176]
    
    if d <= 20:
        spreads= infected[d]
        if n <= spreads:
            print(n)
        else:
            print(spreads)
    else:
        print(n)
