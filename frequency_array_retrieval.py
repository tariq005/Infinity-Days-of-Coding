import collections
for _ in range(int(input())):
    n= int(input())
    b= list(map(int, input().split()))
    val= {}
    freq= collections.Counter(b)
    count= 1
    a= [-1]*n
    
    for i in range(n):
        if freq[b[i]]%b[i] == 0:
            val[b[i]]= count
            count += 1
        if b[i] not in val:
            break
        freq[b[i]] -= 1
        a[i]= val[b[i]]
        
    if min(a) == -1:
        print(-1)
    else:
        print(*a)
