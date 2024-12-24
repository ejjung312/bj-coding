"""
실버 1
다익스트라
"""
import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize

"""
N: 지름길의 개수
D: 고속도로의 길이
"""
N, D = map(int, input().split())

edge = [[] for _ in range(D+1)]
dist = [INF] * (D+1)

for i in range(D):
    edge[i].append([1, i+1])

for _ in range(N):
    start, end, weight = map(int, input().split())
    if end <= D:
        edge[start].append([weight, end])

dist[0] = 0
heap = [[0, 0]]

while heap:
    weight, end = heapq.heappop(heap)
    
    for next_weight, next_end in edge[end]:
        if dist[next_end] > dist[end] + next_weight:
            dist[next_end] = dist[end] + next_weight
            heapq.heappush(heap, [dist[next_end], next_end])

print(dist[D])