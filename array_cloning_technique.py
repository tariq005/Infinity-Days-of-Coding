for _ in range(int(input())):
    n= int(input())
    a= list(map(int, input().split()))
    freq= 1
    curr= 1
    a.sort()

    for i in range(1, n):
        if a[i] == a[i-1]:
            curr += 1
        else:
            curr= 1

        if curr > freq:
            freq= curr

    if n == freq:
        print(0)
    else:
        oper = 0
        n -= freq
        p = 0
        i = 0

        while n > 0:
            p = freq * (2 ** i)
            oper += min(p, n) + 1
            n -= p
            i += 1

        print(oper)