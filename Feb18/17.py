INF = int(1e9)
import heapq
# 단반향이다 다시 돌아오지 못한다. 거쳐서 돌아와야함
N, M ,X = map(int,input().split())
graph = []
for i in range(N+1):
    graph.append([])
for i in range(M):
    v,e,c = map(int,input().split())
    graph[v].append((e,c))
print(graph)
# 최단거리 구하기
def dijkstra(start_node):
    q = []
    visited = [INF] * (N+1)
    heapq.heappush(q,(0,start_node))
    visited[start_node] = 0 
    while q:
        cost, node = heapq.heappop(q)
        for e in graph[node]:
            next_cost = e[1] + cost
            #다음 가려는 곳의 비용이 이전 비용과 비교해서 작을 경우 갱신
            if visited[e[0]] > next_cost:
                visited[e[0]] = next_cost
                heapq.heappush(q,(next_cost,e[0]))
    return visited
answer = 0
for i in range(1,N+1):
    go = dijkstra(i)
    back_home = dijkstra(X)
    # x까지가는데 거리 + X에서 다시 집으로 돌아오는데 거리
    answer = max(answer, go[X] + back_home[i])
print(answer)