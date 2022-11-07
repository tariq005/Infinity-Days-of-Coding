import sys
input= sys.stdin.readline
for _ in range(int(input())):
    n= int(input())
    a= input()
    b= input()
    q= 0
    r= 0
    same= True

    if a == b:
        q= 1
        print('YES')
    else:
        for k in range(n):
            if int(a[k]) != 1-int(b[k]):
                same= False
        if same:
            print('YES')
        else:
            print('NO')
    if same:
        for i in range(n):
            if a[i] == '1':
                r += 1
        if (q+r)%2 == 0:
            print(r+3)
        else:
            print(r)
        for j in range(n):
            if a[j] == '1':
                print(j+1, j+1)
        if (q+r)%2 == 0:
            print(1, 1)
            print(2, n)
            print(1, n)