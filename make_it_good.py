for _ in range(int(input())):
    n= int(input())
    a= list(map(int, input().split()))
    i= n-1

    while i and a[i] <= a[i-1]:
        i -= 1
    while i and a[i] >= a[i-1]:
        i -= 1
    print(i)