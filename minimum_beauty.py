for _ in range(int(input())):
    n= int(input())
    a=sorted(list(map(int, input().split())))
    beauty= 10**10
    
    def f(i, j, k):
        return abs(a[i]+a[k]- 2*a[j])
        
    for i in range(n):
        j= i+1
        for k in range(i+2, n):
            while j+1<k:
                if f(i, j, k)>f(i, j+1, k): j += 1
                else: break
            beauty= min(beauty, f(i, j, k))
            
    print(beauty)
