from collections import deque

n,m = map(int, input().split())

visited = {}
q = deque()
def bfs(i):
    q.append(i)
    visited[i] = 0
    while m not in visited.keys():
        a = q.popleft()
        if visited[a] >= 100000:
            continue
        if a-1>=0 and (a-1) not in visited.keys():
            q.append(a-1)
            visited[a-1] = visited[a]+1
        if a+1 <= 100000 and a+1 not in visited.keys():
            q.append(a+1)
            visited[a+1] = visited[a]+1
        if 2*a <= 100000 and 2*a not in visited.keys():
            q.append(2*a)
            visited[2*a] = visited[a]+1
bfs(n)
print(visited[m])
