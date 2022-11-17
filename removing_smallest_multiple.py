import sys
input= sys.stdin.readline
for _ in range(int(input())):
    n= int(input())
    t= str(input())
    a= list(t)
    ans= 0

    for k in range(1, n+1):
        c= 1
        while c*k <= n:
            if a[c*k-1] == '1':
                break
            elif a[c*k-1] == '0':
                ans += k
                print(ans)
                a[k*c-1]= '-1'
            c += 1

    print(ans)