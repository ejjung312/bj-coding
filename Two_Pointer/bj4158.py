# N, M = map(int, input().split())

# A = [int(input()) for i in range(N)]
# B = [int(input()) for i in range(M)]

# _, _ = map(int, input().split())

# a_p = 0
# b_p = 0
# count = 0

# while a_p < N and b_p < M:
#     if A[a_p] == B[b_p]:
#         count += 1
#         a_p += 1
#         b_p += 1
#     else:
#         if A[a_p] < B[b_p]:
#             a_p += 1
#         else:
#             b_p += 1

# print(count)

"""
sys.stdin.readline() 가 속도 더 빠름
"""

import sys

while True:
    N, M = map(int, sys.stdin.readline().split())
    
    if N == 0 and M == 0:
        break

    A = [int(sys.stdin.readline()) for i in range(N)]
    B = [int(sys.stdin.readline()) for i in range(M)]
    
    a_p = 0
    b_p = 0
    count = 0
    while a_p < N and b_p < M:
        if A[a_p] == B[b_p]:
            count += 1
            a_p += 1
            b_p += 1
        elif A[a_p] < B[b_p]:
            a_p += 1
        else:
            b_p += 1
        
    print(count)