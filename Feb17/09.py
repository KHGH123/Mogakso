from collections import deque

n=int(input())
m=int(input())
edge={}
for i in range(1, n+1):
    edge[i]=[]
visited=set()
for r in range(m):
    x,y=map(int,input().split())
    edge[x].append(y)
    edge[y].append(x)
q=deque()

def bfs(n):
    ans=0
    q.append(n)
    visited.add(n)
    while q:
        k = q.popleft()
        while edge[k]:
            x=edge[k].pop()
            if x not in visited:
                q.append(x)
                visited.add(x)
        ans+=1
    return ans-1
print(bfs(1))