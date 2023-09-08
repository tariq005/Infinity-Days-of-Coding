for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    xorsum = [0]*(n+1)
    for i in range(n):
        xorsum[i+1] = xorsum[i] ^ a[i]

    s = input()
    s = list(s)
    xorzero, xorone = 0, 0
    for j in range(n):
        if s[j] == '0':
            xorzero ^= a[j]
        else:
            xorone ^= a[j]

    for k in range(int(input())):
        q = list(map(int, input().split()))
        if q[0] == 1:
            sum = xorsum[q[2]] ^ xorsum[q[1]-1]
            xorone ^= sum
            xorzero ^= sum
        else:
            if q[1] == 0:
                print(xorzero)
            else:
                print(xorone)
