"""
실버 2
플로이드–워셜
"""
import sys
import pprint

input = sys.stdin.readline

N = int(input())

rs = [list(map(str, input().strip())) for _ in range(N)]
connected = [[0] * (N) for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            
            if (rs[i][k] == 'Y' and rs[k][j] == 'Y') or rs[i][j] == 'Y':
                connected[i][j] = 1
    

answer = 0
for row in connected:
    answer = max(answer, sum(row))
print(answer)