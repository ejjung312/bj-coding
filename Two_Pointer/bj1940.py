import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

A = list(map(int, sys.stdin.readline().split()))

A.sort()

A_s = 0
A_e = N - 1
count = 0

while A_s < A_e:
    total = A[A_s] + A[A_e]
    
    if total < M:
        A_s += 1
    elif total > M:
        A_e -= 1
    else:
        count += 1
        A_s += 1
        A_e -= 1
print(count)