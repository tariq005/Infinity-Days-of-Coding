for _ in range(int(input())):
    n= int(input())
    a= list(map(int, input().split()))
    b= list(map(int, input().split()))
    p= max(a)
    q= max(b)

    if a[-1] == p and q == b[-1]:
        print('YES')
    else:
        for i in range(n):
            if a[i]>b[i]:
                a[i], b[i]= b[i], a[i]

        if a[-1] == max(a) and b[-1] == max(b):
            print('YES')
        else:
            print('NO')