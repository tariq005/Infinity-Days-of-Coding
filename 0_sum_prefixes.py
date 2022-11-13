for _ in range(int(input())):
    n= int(input())
    a= list(map(int, input().split()))
    pref= [0]*(n+1)
    for i in range(1, n+1):
        pref[i]= pref[i-1]+ a[i-1]

    ans= 0
    d= {}
    for j in reversed(range(n)):
        d[pref[j+1]]= d.get(pref[j+1], 0)+ 1
        if a[j] == 0:
            ans += max(d.values())
            d.clear()
    ans += d.get(0, 0)
    print(ans)