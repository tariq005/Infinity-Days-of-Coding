for _ in range(int(input())):
    n= int(input())-1
    build= []
    while n>=0:
        k= int((2*n)**(1/2))**2
        build= list(reversed(range(k-n, n+1)))+ build
        n= k-n-1
    print(*build)