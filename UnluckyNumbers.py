for _ in range(int(input())):
    l, r= map(str, input().split())
    n= len(l)

    if n<len(r):
        print('9'*n)
    else:
        unlucky= l
        minn= int(max(l))- int(min(l))
        for i in range(n):
            for j in range(int(l[i]), int(r[i])+1):
                for k in range(10):
                    c= l[:i]+str(j)+str(k)*(n-i-1)
                    if l <= c <= r and int(max(c))-int(min(c)) <minn:
                        minn= int(max(c))-int(min(c))
                        unlucky= c
                        if minn == 0:
                            break
        print(unlucky)