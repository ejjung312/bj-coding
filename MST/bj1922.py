import sys
import heapq

input = sys.stdin.readline

N = int(input())
M = int(input())

edge = [[] for _ in range(N+1)]
chk = [False] * (N+1)

for _ in range(M):
    a, b, c = map(int, input().split())
    edge[a].append([c, b])
    edge[b].append([c, a])

heap = [[0, 1]]
rs = 0
while heap:
    w, e = heapq.heappop(heap)
    if chk[e] == False:
        chk[e] = True
        rs += w

        for next_edge in edge[e]:
            if chk[next_edge[1]] == False:
                heapq.heappush(heap, next_edge)
                
print(rs)