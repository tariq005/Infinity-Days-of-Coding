from collections import Counter
for _ in range(int(input())):
    n= int(input())
    a= list(map(int, input().split()))
    for i in range(n):
        a[i] -= i
    p= sum([(k*(k-1))//2 for (v, k) in Counter(a).items()])
    print(p)