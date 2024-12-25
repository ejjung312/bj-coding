import sys

input = sys.stdin.readline
"""
N: 사람의 수
P: 인출에 걸리는 시간
"""
N = int(input())
P = list(map(int, input().split()))
result = []

P.sort()

for index, p in enumerate(P):
    if index == 0:
        result.append(p)
    else:
        result.append(result[index-1] + p)

print(sum(result))
