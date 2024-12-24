"""
골드 5
다익스트라
"""
import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize

"""
1: 현서의 위치
N: 헛간의 수, 찬홍의 위치
M: 길의 수
"""
N, M = map(int, input().split())

edge = [[] for _ in range(N+1)]
distance = [INF] * (N+1)

for _ in range(M):
    start, end, weight = map(int, input().split())
    edge[start].append([weight, end])
    edge[end].append([weight, start])

# print(edge)

distance[1] = 0
heap = [[0, 1]]

while heap:
    weight, end = heapq.heappop(heap)
    for next_weight, next_end in edge[end]:
        if weight + next_weight < distance[next_end]:
            distance[next_end] = weight + next_weight
            heapq.heappush(heap, [distance[next_end], next_end])

# print(distance)
print(distance[N])