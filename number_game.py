for i in range(int(input())):
    n= int(input())
    a= list(map(int, input().split()))
    a.sort()
    maxx= 0

    k=1
    while 2*k-2<n:
        i= 2*k-2
        j= k
        while j >= 1:
            if a[i]>j:
                break
            i -= 1
            j -= 1
        if j == 0:
            maxx= k
        else:
            break
        k += 1
    print(maxx)