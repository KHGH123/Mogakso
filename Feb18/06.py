from collections import deque
from sys import stdin

input = stdin.readline
n, m = map(int, input().split())
edge = {}    
visited = set()
ans=0

for r in range(1, n+1):
    edge[r]=[]

for r in range(m):
    x, y = map(int,input().split())
    edge[x].append(y)
    edge[y].append(x)

def bfs(n):
    q = deque()
    q.append(n)
    while q:
        v = q.popleft()
        if v in visited: continue
        visited.add(v)
        for r in edge[v]:
            if r not in visited: q.append(r)

for r in range(1, n+1):
    if r not in visited:
        bfs(r)
        ans+=1

print(ans)