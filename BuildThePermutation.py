for _ in range(int(input())):
    n, a, b= map(int, input().split())

    if a+b+2>n or abs(a-b)>1:
        print(-1)
    else:
        ans= list(range(1, n+1))
        if a == b == 0:
            print(*ans)
        else:
            if a<b:
                for i in range(0, n-1, 2):
                    ans[i], ans[i+1]= ans[i+1], ans[i]
                    b -= 1
                    if b == 0:
                        break
            elif a>b:
                for i in range(n-1, 0, -2):
                    ans[i], ans[i-1]= ans[i-1], ans[i]
                    a -= 1
                    if a == 0:
                        break
            else:
                for i in range(0, n-1, 2):
                    ans[i], ans[i+1]= ans[i+1], ans[i]
                    a -= 1
                    if a == 0:
                        break

                ans[-1], ans[-2]= ans[-2], ans[-1]
            print(*ans)