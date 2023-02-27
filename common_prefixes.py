for _ in range(int(input())):
    n= int(input())
    a= list(map(int, input().split()))
    s= ['a']*(max(a)+1)
    print(''.join(s))

    for i in range(n):
        p= s
        if p[a[i]] == 'a':
            p[a[i]]= 'b'
        else:
            p[a[i]]= 'a'
        print(''.join(p))