for _ in range(int(input())):
    n= int(input())
    a= list(map(int, input().split()))

    if len(set(a)) == 1:
        print(0)
    elif len(set(a)) == n:
        print(1)
    else:
        b= [a[0]]
        for i in range(1, n):
            if a[i] != a[i-1]:
                b.append(a[i])

        dic= {}
        for x in b:
            if x in dic:
                dic[x] += 1
            else:
                dic[x]= 1
        dic[b[len(b)-1]] -= 1
        dic[b[0]] -= 1
        print(min(dic.values())+1)