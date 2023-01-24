for _ in range(int(input())):
    d= int(input())
    b= {}
    for i in range(d):
        n, p= map(int, input().split())
        b[n]= p
    q= int(input())
    for j in range(q):
        dead, req= map(int, input().split())
        solved= 0
        for k in b.keys():
            if k <= dead:
                solved += b[k]
            else:
                break
        print('Go Camp' if solved >= req else 'Go Sleep')
