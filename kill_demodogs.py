for _ in range(int(input())):
    n= int(input())
    print(((2*n*(n+1)*(2*n+1))//6+ (n*(n+1))//2 -n*n- n)* 2022% 1000000007)