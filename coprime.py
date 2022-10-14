from math import gcd
for i in range(int(input())):
    n= int(input())
    b= [0]*1001
    maxx= 0

    for i, a in enumerate(map(int, input().split())):
        b[a] = i + 1

    for j in range(1, 1001):
        if b[j] > 0:
            for k in range(j, 1001):
                if b[k] > 0 and gcd(j,k) == 1:
                    maxx= max(maxx, b[j]+ b[k])

    if maxx == 0:
        print(-1)
    else:
        print(maxx)