import sys
input= sys.stdin.readline
for _ in range(int(input())):
    n= int(input())
    a= list(map(int, input().split()))
    p, q= [0]*n, [0]*n
    pos= [[] for i in range(n+1)]
    for i in range(n):
        pos[a[i]].append(i)
    rp, rq= [], []
    for i in range(n, 0, -1):
        if len(pos[i]) == 2:
            p[pos[i][0]]= i
            q[pos[i][1]]= i
            rp.append(pos[i][1])
            rq.append(pos[i][0])
        elif len(pos[i]) == 1:
            p[pos[i][0]]= i
            q[pos[i][0]]= i
        elif len(rp)>0 and len(rq)>0:
            p[rp.pop()]= i
            q[rq.pop()]= i
        else:
            print('NO')
            break
    else:
        print('YES')
        print(*p)
        print(*q)