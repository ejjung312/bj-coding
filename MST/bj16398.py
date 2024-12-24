import sys

input = sys.stdin.readline

N = int(input())
parent = [i for i in range(N+1)]
graph = [list(map(int, input().split())) for _ in range(N)]

list = []
for a in range(N):
    for b in range(a+1, N):
        list.append([graph[a][b], a, b])

list.sort()

total_cost = 0

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    rootA = find(parent, a)
    rootB = find(parent, b)
    
    if rootA < rootB:
        parent[rootB] = rootA
    else:
        parent[rootA] = rootB

for weight, a, b in list:
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        total_cost += weight

print(total_cost)