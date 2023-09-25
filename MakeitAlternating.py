from math import factorial
for _ in range(int(input())):
    s = input()
    n = len(s)
    count, ans = 0, 1
    mod = 998244353
    i, j = 0, 1

    while i < n:
        while j < n and s[j] == s[i]:
            j += 1
        if j-i-1 > 0:
            count += j - i - 1
            q = j-i
            q %= mod
            ans *= q
            ans %= mod
        i = j
    print(count, (ans*(factorial(count) % mod) % mod))
