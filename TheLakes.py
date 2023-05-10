from collections import deque
changex = [0, 1, 0, -1]
changey = [1, 0, -1, 0]

def bfs(i, j, n, m, a, visited):
    visited[i][j] = True
    value = a[i][j]
    q = deque([(i, j)])
    while q:
        x, y = q.popleft()
        for k in range(4):
            newx, newy = x+changex[k], y+changey[k]
            if newx < 0 or newy < 0 or newx >= n or newy >= m or visited[newx][newy]:
                continue
            value += a[newx][newy]
            visited[newx][newy] = True
            q.append((newx, newy))
    return value


for _ in range(int(input())):
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for i in range(n)]
    visited = [[a[i][j] == 0 for j in range(m)] for i in range(n)]
    ans = 0

    for i in range(n):
        for j in range(m):
            if visited[i][j]:
                continue
            ans = max(ans, bfs(i, j, n, m, a, visited))
    print(ans)
