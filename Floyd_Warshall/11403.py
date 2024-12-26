"""
실버 1
플로이드–워셜
"""
import sys

input = sys.stdin.readline

N = int(input())

rs = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        for k in range(N):
            if rs[j][i] and rs[i][k]:
                rs[j][k] = 1
                
for r in rs:
    print(*r)