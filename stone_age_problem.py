import sys
input= sys.stdin.readline
n, q= map(int, input().split())
a= list(map(int, input().split()))
p= sum(a)
dic= {}
for i in range(n):
    dic[i+1]= a[i]

for _ in range(q):
    s= list(map(int, input().split()))
    if s[0] == 1:
        p += s[2]- dic.get(s[1], q)
        dic[s[1]]= s[2]
    else:
        q= s[1]
        p= n*q
        dic.clear()
    print(p)