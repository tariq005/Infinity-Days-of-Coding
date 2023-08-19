from math import sqrt
n = int(input())
a = [1, n*(n+1)//2]

for i in range(2, int(sqrt(n))+1):
    if n % i == 0:
        p = i
        q = n//i
        a.append(i*(q*(q-1)//2)+q)

        if p != q:
            a.append(q*(p*(p-1)//2)+p)
a.sort()
print(*a)
