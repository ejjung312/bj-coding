"""
골드 4
플로이드–워셜
"""
import sys

input = sys.stdin.readline
INF = sys.maxsize

n = int(input())
m = int(input())

rs = [[INF] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    rs[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    rs[a][b] = min(rs[a][b], c)

for k in range(n+1):
    for i in range(n+1):
        for j in range(n+1):
            if rs[i][j] > rs[i][k] + rs[k][j]:
                rs[i][j] = rs[i][k] + rs[k][j]
                
for i in range(1, n+1):
    for j in range(1, n+1):
        if rs[i][j] == INF: print(0, end=' ')
        else: print(rs[i][j], end=' ')
    print()