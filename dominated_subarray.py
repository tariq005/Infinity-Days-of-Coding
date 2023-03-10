for _ in range(int(input())):
    n= int(input())
    a= list(map(int, input().split()))

    if len(set(a)) == n:
        print(-1)
    else:
        dic= {}
        minn= n
        for i in range(n):
            if a[i] in dic:
                minn= min(minn, i-dic[a[i]][-1]+1)
                dic[a[i]].append(i)
            else:
                dic[a[i]]= [i]
        print(minn)