from numpy import array, trace
for i in range(int(input())):
    n = int(input())
    a = []

    for j in range(n):
        u = list(map(int, input().split()))
        a.extend(u)

    matrix = array(a).reshape(n, n)
    maxx = 0

    for k in range(n):
        for m in range(n):
            s = matrix[k:, m:]
            traced = trace(s)
            maxx= max(traced, maxx)

    print(maxx)