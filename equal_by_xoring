from math import log, pow
for _ in range(int(input())):
    a, b, n= map(int, input().split())
    c= a^b
    
    if c == 0:
        print(0)
    elif c<n:
        print(1)
    elif pow(2, int(log(c, 2)))<n:
        print(2)
    else:
        print(-1)
