for _ in range(int(input())):
    n, k= map(int, input().split())
    a= list(map(int, input().split()))
    b= list(map(int, input().split()))
    s= []
    for i in range(n):
        s.append(a[i]+b[i])
    s.sort()
    
    count= 0
    r= k
    for i in range(n):
        if s[i]>r:
            break
        r -= s[i]
        count += 1
        
    if count == n:
        print(count)
    else:
        for j in range(n):
            if a[j] <= r:
                if a[j]+b[j] >= s[i] or r+b[j]-s[i] >= 0:
                    count += 1
                    break
        print(count)
