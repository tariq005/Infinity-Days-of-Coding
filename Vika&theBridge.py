for _ in range(int(input())):
    n, k = map(int, input().split())
    c = list(map(int, input().split()))
    last = [-1]*k
    max1 = [0]*k
    max2 = [0]*k

    for i in range(n):
        diff = i-last[c[i]-1]-1
        if diff > max1[c[i]-1]:
            max2[c[i]-1] = max1[c[i]-1]
            max1[c[i]-1] = diff
        elif diff > max2[c[i]-1]:
            max2[c[i]-1] = diff
        last[c[i]-1] = i

    for i in range(k):
        diff = n-last[i]-1
        if diff > max1[i]:
            max2[i] = max1[i]
            max1[i] = diff
        elif diff > max2[i]:
            max2[i] = diff

    ans = 1000000
    for i in range(k):
        ans = min(ans, max((max1[i])//2, max2[i]))
    print(ans)
