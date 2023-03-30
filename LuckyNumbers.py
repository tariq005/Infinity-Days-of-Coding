for _ in range(int(input())):
    l, r= map(int, input().split())
    diff, x= 0, l
    for i in range(l, r+1):
        s= str(i)
        p= int(max(s))-int(min(s))
        if p>diff:
            diff= p
            x= i
        if diff == 9:
            break
    print(x)
