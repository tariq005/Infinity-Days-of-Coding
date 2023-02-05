for _ in range(int(input())):
    n= int(input())
    a= list(map(int, input().split()))

    i= (n+1)//2
    j= (n+2)//2
    while i>0 and i == j or (a.index(i)<a.index(j)):
        i -= 1
        j += 1

    print(i)