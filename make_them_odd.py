for _ in range(int(input())):
    n= int(input())
    a= list(map(int, input().split()))
    a.sort(reverse= True)
    dic= {}
    odd= 0

    for x in a:
        if x not in dic:
            n= 0
            dic[x]= 1
            while x%2 == 0:
                x //= 2
                dic[x]= 1
                n += 1
            odd += n
    print(odd)