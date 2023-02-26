for _ in range(int(input())):
    a, b= map(int, input().split())
    n= a+b
    s= list(input())
    for i in range(n):
        if s[i] == '?':
            s[i]= s[n-i-1]

    a -= s.count('0')
    b -= s.count('1')
    for i in range(n//2 +1):
        if s[i] == '?' and i != n//2:
            if a>1:
                s[i]= s[n-i-1]= '0'
                a -= 2
            elif b>1:
                s[i]= s[n-i-1]= '1'
                b -= 2
        elif s[i] == '?':
            if a>0:
                s[i]= '0'
                a -= 1
            elif b>0:
                s[i]= '1'
                b -= 1

    if s == s[::-1] and a == b == 0:
        print(''.join(s))
    else:
        print(-1)