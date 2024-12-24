"""
골드 4
다익스트라
"""
import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize
"""
V: 정점의 개수
E: 간선의 개수
K: 시작 정점 번호
"""
V, E = map(int, input().split())
K = int(input())

edge = [[] for _ in range(V+1)]
distance = [INF] * (V+1)

for _ in range(E):
    # u->v 가중치 w
    u, v, w = map(int, input().split())
    edge[u].append([w, v])

distance[K] = 0
heap = [[0, K]]

while heap:
    current_weight, current_node = heapq.heappop(heap)
    if distance[current_node] != current_weight:
        continue
    for next_weight, next_node in edge[current_node]:
        if next_weight + current_weight < distance[next_node]:
            distance[next_node] = next_weight + current_weight
            heapq.heappush(heap, [distance[next_node], next_node])

for i in range(1, V+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])