"""
실버 1
플로이드–워셜
"""
import sys
import pprint

input = sys.stdin.readline
INF = sys.maxsize

N, M = map(int, input().split())

rs = [[INF] * (N+1) for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    rs[a][b] = 1
    rs[b][a] = 1
    
for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if i == j:
                rs[i][j] = 0
            else:
                rs[i][j] = min(rs[i][j], rs[i][k]+rs[k][j])

result = []
for row in rs:
    result.append(sum(row))
print(result.index(min(result)))