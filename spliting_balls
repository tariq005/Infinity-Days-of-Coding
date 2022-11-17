m= 10**9 + 7
fact= [1]
for i in range(1, (10**6)+ 1):
    next= fact[-1]*i
    fact.append(next%m)

for _ in range(int(input())):
    n= int(input())
    a= list(map(int, input().split()))
    
    d= 0
    for k in a:
        d= (d+fact[k])%m
        
    print(d)
