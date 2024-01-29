import bisect
for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    if k >= 3:
        print(0)
        continue
    arr.sort()
    ans = arr[0]
    for i in range(1, n):
        ans = min(ans, arr[i] - arr[i - 1])
    if k == 1:
        print(ans)
    elif k == 2:
        for i in range(n):
            for j in range(i):
                have = arr[i] - arr[j]
                index = bisect.bisect_left(arr, have)
                if index < n:
                    ans = min(ans, abs(arr[index] - have))
                if index > 0:
                    ans = min(ans, abs(arr[index - 1] - have))
        print(ans)
