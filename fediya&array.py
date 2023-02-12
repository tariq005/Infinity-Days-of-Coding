for _ in range(int(input())):
    x, y= map(int, input().split())
    a= list(range(y, x))
    b= [x]+ a[::-1]
    c= b[::-1]
    d= c[1:-1]
    f= b+d
    print(len(f))
    print(*f)