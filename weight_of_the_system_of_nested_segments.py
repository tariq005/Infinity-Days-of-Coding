import sys
input= sys.stdin.readline
for _ in range(int(input())):
    input()
    a= []
    n, m= map(int, input().split())
    for i in range(m):
        x, w= map(int, input().split())
        a.append((i+1, x, w))

    a.sort(key=lambda x: x[2])
    a= a[:2*n]
    a.sort(key=lambda x: x[1])
    b= []
    sum= 0
    for p,q,r in a:
        b.append(p)
        sum += r

    print(sum)
    i= 0
    j= len(b)-1
    while i<j:
        print(b[i], b[j])
        i += 1
        j -= 1