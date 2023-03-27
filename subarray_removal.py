for _ in range(int(input())):
    n= int(input())
    a= list(map(int, input().split()))
    one= a.count(1)
    zero= a.count(0)
    ans= min(one, zero)
    
    one -= ans
    zero -= ans
    one= max(one, one- zero)
    print(ans+ one//3)
