n= 100000
pre= [0]*(n+1)
c= 1
while c<(n//2)+1:
    b= c
    while b<(n+1):
        if (b%c) == 0:
            a= c
            while a<(n+1):
                if (a%b) == c:
                    if a>b:
                        pre[a] += 1
                    elif a<b:
                        pre[b] += 1
                else:
                    break
                a += b
        else:
            break
        b += c
    c += 1
                        
for _ in range(int(input())):
    n= int(input())
    print(sum(pre[:(n+1)]))
