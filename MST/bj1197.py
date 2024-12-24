import sys
import heapq

input = sys.stdin.readline

V, E = map(int, input().split())
list = [[] for _ in range(V+1)]
chk = [False] * (V+1)

for _ in range(E):
    A, B, C = map(int, input().split())
    list[A].append([C, B])
    list[B].append([C, A])

heap = [[0, 1]]
rs = 0
while heap:
    weight, edge = heapq.heappop(heap)
    if chk[edge] == False:
        chk[edge] = True
        rs += weight
        
        for next_edge in list[edge]:
            if chk[next_edge[1]] == False:
                heapq.heappush(heap, next_edge)

print(rs)