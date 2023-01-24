for _ in range(int(input())):
    n = int(input())
    a = []
    for i in range(n):
        b = list(map(int, input().split()))
        for j, d in enumerate(b):
            a.append((d, i, j))
    a.sort(key=lambda x: x[0])
    steps = 0 
    for y, i, j in a:
        if y > 1:
            steps += abs(i - pi) + abs(j - pj)
        pi = i; pj = j
    print(steps)
