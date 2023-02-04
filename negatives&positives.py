for _ in range(int(input())):
    n= int(input())
    a= list(map(int, input().split()))
    neg= 0

    for i in range(n):
        if a[i]<0:
            neg += 1
            a[i]= abs(a[i])

    p= sum(a)
    if neg%2:
        print(p -min(a)*2)
    else:
        print(p)