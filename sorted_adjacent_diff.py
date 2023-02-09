for _ in range(int(input())):
    n= int(input())
    a= sorted(list(map(int, input().split())))
    while n>0:
        print(a.pop(n//2), end= ' ')
        n -= 1