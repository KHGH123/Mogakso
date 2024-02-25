from collections import deque

n=int(input())
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
#     상 하 좌 우

for i in range(n):
    ans=0
    a=[*map(int, input().split())]
    b=[]
    for r in range(a[2]):
        b.append([*map(int, input().split())])
    visited={}
    def bfs(n):
        global ans
        q = deque()
        q.append((n[0],n[1]))
        visited[(n[0],n[1])]=0
        while q:
            bb=q.popleft()
            x=bb[0]
            y=bb[1]
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                if nx < 0 or ny < 0 or nx >= a[0] or ny >= a[1]:
                    continue
                elif (nx, ny) in visited.keys() or [nx, ny] not in b:
                    continue
                else:
                    visited[(nx, ny)] = 0
                    q.append((nx,ny))
        
    while len(b) != 0:
        k=b.pop()
        if (k[0], k[1]) not in visited:
            bfs(k)
            ans+=1

    print(ans)
                            
