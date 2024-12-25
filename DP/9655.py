import sys

input = sys.stdin.readline

N = int(input())

dp = [0] * (N+1)

dp[1] = 1
dp[2] = 2
dp[3] = 1

for i in range(4, N+1):
    dp[i] = min(dp[i-1], dp[i-3]) + 1

if dp[N] % 2 == 0:
    print("CY")
else:
    print("SK")

"""
상근: SK
창영: CY
상근이 먼저 시작
돌은 1개 또는 3개를 가져감
마지막 돌을 가져가는 사람이 이김
"""
