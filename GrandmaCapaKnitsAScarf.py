for _ in range(int(input())):
    n= int(input())
    s= input()

    if s == s[::-1]:
        print(0)
    else:
        count= 1e5
        for i in range(26):
            c= chr(ord('a')+i)
            l, r, erased= 0, n-1, 0
            while l<r:
                if s[l] == s[r]:
                    r -= 1
                    l += 1
                else:
                    if s[l] == c:
                        erased += 1
                        l += 1
                    elif s[r] == c:
                        erased += 1
                        r -= 1
                    else:
                        erased= 1e5
                        break
            count= min(count, erased)
        print(-1) if count == 1e5 else print(count)