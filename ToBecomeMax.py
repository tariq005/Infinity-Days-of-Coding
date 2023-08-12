def possible(z, p, b):
    for i in range(len(b)-1):
        rem = p
        target = z
        j = i

        while True:
            if j == n or rem < 0:
                break
            if b[j] >= target:
                return True
            rem -= target-b[j]
            j += 1
            target -= 1


for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    low, high = max(a), max(a)+k
    ans = max(a)

    while low <= high:
        x = low+(high-low)//2
        if possible(x, k, a):
            ans = x
            low = x+1
        else:
            high = x-1
    print(ans)
