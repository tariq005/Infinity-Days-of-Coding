for _ in range(int(input())):
    n = int(input())
    
    if n%2:
        if n == 1:
            print(1)
        else:
            odd, even = 1, 2
            for i in range(1, n+1):
                a = []
                p = n-i
                if i%2:
                    p += 1
                j = 0
                while j < p:
                    a.append(odd)
                    odd += 2
                    j += 1
                k = 0
                while k < n-p:
                    a.append(even)
                    even += 2
                    k += 1
                print(*a)
    else:
        odd, even = 1, 2
        p = n//2
        for i in range(1, p+1):
            a = []
            b = []
            for k in range(i-1):
                a.append(even)
                even += 2
            for j in range(n-2*i+1):
                a.append(odd)
                odd += 2
            for k in range(i):
                a.append(even)
                even += 2
            for k in range(i-1):
                b.append(even)
                even += 2
            for j in range(n-2*i+1):
                b.append(odd)
                odd += 2
            for k in range(i):
                b.append(even)
                even += 2
            b = b[::-1]
            print(*a)
            print(*b)
