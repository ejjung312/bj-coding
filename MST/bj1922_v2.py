import sys

input = sys.stdin.readline

N = int(input())
M = int(input())

list = []
for _ in range(M):
    a, b, c = map(int, input().split())
    list.append([c, a, b])

list.sort()

parent = [i for i in range(N+1)]

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

print(list)
print(total_cost)