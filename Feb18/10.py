from collections import deque


n, m = map(int, input().split())

k = []

dx=[0, 0, -1, 1]
dy=[-1, 1, 0, 0]

x, y =0, 0
for i in range(n):
    k.append([*map(int, input().split())])

print(k)
g = [[-1] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if k[i][j] == 2:
            x, y = i, j
            break
g[x][y]=0
def bfs(x, y):
    q = deque()
    q.append((x,y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >=m:
                continue

            if k[nx][ny] == 0:
                continue
            if g[nx][ny] == -1:
                g[nx][ny] = g[x][y]+1
                q.append((nx,ny))

    for i in range(n):
        for j in range(m):
            if k[i][j] == 0: g[i][j] = 0
bfs(x, y)
for r in g: print(*r)