for _ in range(int(input())):
    n, d= map(int, input().split())
    s= input()
    d= str(d)

    if d > s[0]:
        print(d+s)
    elif d == '0':
        print(s+d)
    else:
        for i in range(n-1):
            if int(s[i]+d)>int(s[i:i+2]):
                print(s[:i+1]+d+s[i+1:])
                break
        else:
            print(s+d)