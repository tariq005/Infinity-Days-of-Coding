from math import factorial
def nCr(b, x):
    return factorial(b)//(factorial(x)*factorial(b-x))

x, n= map(int, input().split())
c= 0
for i in range(n):
    a= input()
    for j in range(9):
        s= a[:4]+a[-2:]
        a= a[4:-2]
        b= s.count('0')
        if b >= x:
            c += nCr(b, x)
print(c)