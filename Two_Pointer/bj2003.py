import sys

# N개의 수열, 합이 M이 되는 경우
N, M = map(int, sys.stdin.readline().split())

A = list(map(int, sys.stdin.readline().split()))

A_s = 0
A_e = 1
count = 0

while A_s <= N and A_e <= N:
    total = sum(A[A_s:A_e])
    
    if total < M:
        A_e += 1
    elif total > M:
        A_s += 1
    else:
        count += 1
        A_e += 1
print(count)