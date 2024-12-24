"""
골드 5
다익스트라
"""
import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize

"""
N: 도시의 개수
M: 버스의 개수
"""
N = int(input())
M = int(input())

edge = [[] for _ in range(N+1)]
distance = [INF] * (N+1)

for _ in range(M):
    start, end, weight = map(int, input().split())
    edge[start].append([weight, end])

"""
출발 도시번호, 도착 도시번호
"""
dest_start, dest_end = map(int, input().split())
distance[dest_start] = 0

heap = [[0, dest_start]]
while heap:
    current_weight, current_end = heapq.heappop(heap)
    if current_weight != distance[current_end]:
        continue
    for next_weight, next_end in edge[current_end]:
        if current_weight + next_weight < distance[next_end]:
            distance[next_end] = current_weight + next_weight
            heapq.heappush(heap, [distance[next_end], next_end])

print(distance[dest_end])