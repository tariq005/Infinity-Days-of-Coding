for _ in range(int(input())):
    n, m, d= map(int, input().split())
    p= list(map(int, input().split()))
    a= list(map(int, input().split()))
    pos= [0]*(n+1)
    min_move= n

    for i in range(n):
        x= p[i]
        pos[x]= i+1

    for i in range(m-1):
        if pos[a[i]] > pos[a[i+1]]:
            min_move= 0
            break
        elif pos[a[i]]+d < pos[a[i+1]]:
            min_move= 0
            break
        else:
            min_move= min(min_move, pos[a[i+1]]- pos[a[i]])
            moves= d-(pos[a[i+1]]- pos[a[i]])+ 1
            if moves <= pos[a[i]]-1+n-pos[a[i+1]]:
                min_move= min(min_move, moves)

    print(min_move)