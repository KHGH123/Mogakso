from collections import deque

n, m = map(int, input().split())

k = []

dx=[0, 0, -1, 1]
dy=[-1, 1, 0, 0]

for ii in range(m):
    k.append([*map(int, input().split())])

h = [(i, j) for i in range(m) for j in range(n) if k[i][j] == 1]

def bfs(h):
    ans = 1
    q = deque()
    for r in h:
        q.append(r)
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if k[nx][ny] != 0:
                continue
            k[nx][ny] = k[x][y]+1
            if ans < k[nx][ny] : ans = k[nx][ny]
            q.append((nx,ny))
    return ans-1

ans = bfs(h)
for i in range(m):
    if 0 in k[i]:
        print(-1)
        exit()
print(ans)
