from math import *
for _ in range(int(input())):
    n= int(input())
    m= int(log2(n))
    print(max(n+1-(2**m), (2**m)- 2**(m-1)))
