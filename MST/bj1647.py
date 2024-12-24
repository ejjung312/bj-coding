# import sys
# import heapq

# input = sys.stdin.readline

# N, M = map(int, input().split())
# list = [[] for _ in range(N+1)]
# chk = [False] * (N+1)

# for _ in range(M):
#     A, B, C = map(int, input().split())
#     list[A].append([C, B])
#     list[B].append([C, A])

# heap = [[0, 1]]
# total_cost = 0
# max_weight = 0

# while heap:
#     weight, edge = heapq.heappop(heap)
    
#     if chk[edge]:
#         continue
    
#     chk[edge] = True
#     total_cost += weight
#     max_weight = max(max_weight, weight)
    
#     for next_weight, next_node in list[edge]:
#         if not chk[next_node]:
#             heapq.heappush(heap, [next_weight, next_node])

# print(total_cost - max_weight)

"""
크루스칼 알고리즘
"""
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
list = []

for _ in range(M):
    A, B, C = map(int, input().split())
    list.append([C, A, B])
    
list.sort()

parent = [i for i in range(N+1)]

total_cost = 0
max_weight = 0

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x]) # 경로압축
    return parent[x]

def union(parent, a, b):
    rootA = find(parent, a)
    rootB = find(parent, b)
    
    if rootA < rootB:
        parent[rootB] = rootA
    else:
        parent[rootA] = rootB

for weight, a, b in list:
    if find(parent, a) != find(parent, b): # 두 집이 연결되어 있지 않다면
        union(parent, a, b) # 두 집을 연결
        total_cost += weight
        max_weight = max(max_weight, weight)
        
print(total_cost - max_weight)