for _ in range(int(input())):
    m, k, a, b = map(int, input().split())
    m -= k*b
    if m < 0:
        m %= k
    m -= a
    if m <= 0:
        print(0)
    else:
        if k-(m % k) <= a and (m % k):
            print((m//k) + 1)
        else:
            print((m//k) + (m % k))
