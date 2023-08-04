for _ in range(int(input())):
    n, k = map(int, input().split())

    if k >= 29:
        print(0)
    else:
        ans = 0
        for i in range(n+1):
            first = n
            second = i
            value = True
            for j in range(k-2):
                temp = first-second
                first = second
                second = temp
                value &= min(first, second) >= 0
                value &= first >= second
                if not value:
                    break
            if value:
                ans += 1
        print(ans)
