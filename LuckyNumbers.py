for _ in range(int(input())):
    l, r= map(str, input().split())
    a, b, diff, x= int(l), int(r), 0, int(l)
    for i in range(a, b+1):
        s= str(i)
        p= int(max(s))-int(min(s))
        if p>diff:
            diff= p
            x= i
        if diff == 9:
            break
    print(x)