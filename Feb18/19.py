from collections import deque
import random

n = int(input())
a = [*map(int, input().split())]

a = [random.randrange(1, 1001) for _ in range(50)]
n = 50

m = [[] for _ in range(n)]
q = deque()
v = set()
q.append(([a[0]], 0))
m[0].append([a[0]])
while q:
    graph, idx = q.popleft()
    if ((*graph, idx)) in v:
        continue
    v.add((*graph, idx))
    
    if len(graph) != 1 and graph[-1] < graph[-2]:
        temp = graph[:-2]+[graph[-1]]
        # m[len(temp)-1].append(temp)
        q.append((temp, idx))
        q.append((graph[:-1], idx))
    elif len(graph) != 1 and graph[-1] == graph[-2]:
        temp = []+graph[:-1]
        # m[len(temp)-1].append(temp)
        q.append((temp, idx))
    else:
        if idx >= n-1: continue
        k = a[idx+1]
        if graph[-1] < k:
            m[len(graph)].append(graph+[k])
        q.append((graph+[k], idx+1))

for i in range(n):
    if m[i]==[]:
        print(i, m[i-1])
        break