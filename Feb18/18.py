from sys import stdin
input = stdin.readline

import heapq
v, e = map(int, input().split())
start_node = int(input())

graph = [[] for _ in range(v+1)]

for i in range(e):
    x, y, z = map(int, input().split())
    graph[x].append([y, z])

def func(sn):
    q=[]
    visited = [float("inf") for _ in range(v+1)]

    heapq.heappush(q, (0, sn))
    visited[sn] = 0

    while q:
        cost, node = heapq.heappop(q)

        for x in graph[node]:
            nc = x[1] + cost
            if visited[x[0]] > nc:
                visited[x[0]] = nc
                heapq.heappush(q, (nc, x[0]))
    return visited

answer = func(start_node)
for i in range(1, v+1):
    if answer[i] == float("inf"): print("INF")
    else: print(answer[i])
    