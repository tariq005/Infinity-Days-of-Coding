import sys
input= sys.stdin.readline
for _ in range(int(input())):
    n= int(input())
    a= {}
    i= 2

    while i*i <= n:
        while n%i == 0:
            if i not in a:
                a[i]= 1
            else:
                a[i] += 1
            n //= i
        i += 1
    if n>1:
        if n in a:
            a[n] += 1
        else:
            a[n]= 1

    factor= 1
    prime= 0
    while len(set(a.values())) >=1:
        if len(set(a.values())) == 1 and 0 in set(a.values()):
            break
        else:
            for x in a:
                if a[x]>0:
                    factor *= x
                    a[x] -= 1
            prime += factor
            factor= 1

    print(prime)
