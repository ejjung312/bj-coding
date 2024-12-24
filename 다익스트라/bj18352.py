"""
실버 2
다익스트라
"""

import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize

"""
N: 도시의 개수
M: 도로의 개수
K: 거리 정보
X: 출발 도시
"""
N, M, K, X = map(int, input().split())

edge = [[] for _ in range(N+1)]
distance = [INF] * (N+1)
distance[X] = 0

for _ in range(M):
    A, B = map(int, input().split())
    edge[A].append([1, B])

heap = [[0, X]]
while heap:
    current_weight, current_node = heapq.heappop(heap)
    if current_weight != distance[current_node]:
        continue
    for next_weight, next_node in edge[current_node]:
        if current_weight + next_weight < distance[next_node]:
            distance[next_node] = current_weight + next_weight
            heapq.heappush(heap, [distance[next_node], next_node])

node_list = []
for i in range(1, N+1):
    if distance[i] == K:
        node_list.append(i)
node_list.sort()

if len(node_list) == 0:
    print(-1)
else:
    for i in node_list:
        print(i)