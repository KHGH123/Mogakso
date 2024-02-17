from collections import deque


n, m = list(map(int, input().split()))
mm=[]
for r in range(n):
    mm.append(list(map(int, str(input()))))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
# 상 하 좌 우

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m :
                continue
            if mm[nx][ny] == 0:
                continue
            if mm[nx][ny] == 1:
                mm[nx][ny] = mm[x][y]+1
                queue.append((nx, ny))
    return mm[n-1][m-1]

print(bfs(0,0))