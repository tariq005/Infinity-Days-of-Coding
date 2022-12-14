for _ in range(int(input())):
    n= int(input())
    a= list(map(int, input().split()))

    n += 1
    a.append(0)
    nit= 0
    for i in range(n-1):
        if a[i] != 0 and a[i+1] == 0:
            nit += 1

    if nit == 1:
        print(1)
    elif nit == 0:
        print(0)
    else:
        print(2)