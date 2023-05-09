for _ in range(int(input())):
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    left = x.count(-1)
    right = x.count(-2)
    neutral = [0]*m

    for a in x:
        if a > 0:
            neutral[a-1] = 1
    mid = neutral.count(1)

    if mid == 0:
        print(min(max(left, right), m))
    elif left == 0:
        print(min(right+mid, m))
    elif right == 0:
        print(min(left+mid, m))
    else:
        ans = mid
        count = 0
        for i in range(m):
            if neutral[i] == 1:
                c = min(left, i-count)
                d = min(right, m-i-(mid-count))
                ans = max(ans, mid+c+d)
                count += 1
        c = min(left+mid, m)
        d = min(right+mid, m)
        print(max(ans, c, d))
