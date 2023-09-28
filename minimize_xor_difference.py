for _ in range(int(input())):
    a, b = map(int, input().split())
    
    if a == b:
        print(0)
    else:
        if a<b:
            a, b = b, a
        for i in range(29, -1, -1):
            x = 1<<i
            if a&x != b&x:
                bit = i
                break
            
        ans = 0
        for i in range(bit-1, -1, -1):
            x = 1<<i
            if (a&x)>0 & (b&x)==0:
                ans += x
        print(ans)
    
