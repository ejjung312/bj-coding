import sys

input = sys.stdin.readline

N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]

coins.reverse()
count = 0

for coin in coins:
    count += K // coin
    K = K % coin

print(count)