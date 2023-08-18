for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    first_min = a[0]
    sec_min = 1000000000
    ans = 0

    for i in range(1, n):
        if (first_min < a[i]) and (a[i] < sec_min):
            ans += 1
            sec_min = a[i]
        if a[i] < first_min:
            first_min = a[i]
    print(ans)
