for i in range(int(input())):
    n= int(input())
    a= list(map(int, input().split()))
    b= list(map(int, input().split()))

    u= 0
    for j in range(n):
        if a[j] != b[j]:
            u += 1

    if (abs(a.count(1)- b.count(1))) == u:
        print(abs(a.count(1)- b.count(1)))
    else:
        print(abs(a.count(1)- b.count(1)) +1)
                