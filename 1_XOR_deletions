for i in range(int(input())):
    n= int(input())
    a= list(map(int, input().split()))
    dic= {}
    
    for x in a:
        if x in dic:
            dic[x] += 1
        else:
            dic[x]= 1
            
    ndel= n
    for x in dic:
        if x^1 in dic:
            ndel= min(ndel, n-dic[x]-dic[x^1])
        else:
            ndel= min(ndel, n-dic[x])
    
    print(ndel)
