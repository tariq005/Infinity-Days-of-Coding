for _ in range(int(input())):
    a, b, c, d= map(int, input().split())
    
    if d <= a:
        ans= 0
    else:
        x= max(a, c)
        y= min(b, d)
        ans= (y-a+1)*(d-x+1)
        if y >= x:
            g= y-x+1
            ans -= ((g*(g+1))//2)
    print(ans)
