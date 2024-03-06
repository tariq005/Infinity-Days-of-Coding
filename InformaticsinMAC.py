for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    if len(set(a)) == 1:
        print(n)
        for i in range(n):
            print(i+1, i+1)
    else:
        mp1 = {}
        mp2 = {}
        pre = [0] * n
        suff = [0] * n
        curr = 0

        for i in range(n):
            mp1[a[i]] = 1
            while curr in mp1:
                curr += 1
            pre[i] = curr

        curr = 0
        for i in range(n - 1, -1, -1):
            mp2[a[i]] = 1
            while curr in mp2:
                curr += 1
            suff[i] = curr

        for i in range(n-1):
            if pre[i] == suff[i+1]:
                print(2)
                print(1, i+1)
                print(i+2, n)
                break
        else:
            print(-1)
