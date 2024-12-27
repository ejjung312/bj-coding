"""
실버 5
"""

import sys
import pprint

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    # 서쪽, 동쪽
    N, M = map(int, input().split())
    
    rs = [[0 for _ in range(M+1)] for _ in range(N+1)]
    
    for j in range(1, M+1):
        rs[1][j] = j
        rs[0][j] = 1
    
    for i in range(2, N+1):
        for j in range(i, M+1):
            rs[i][j] = rs[i-1][j-1] + rs[i][j-1]
    
    print(rs[N][M])
"""
M = M-1 + M-1
N   N-1    N

5 = 4 + 4
2   1   2

4 = 3 + 3
1   0   1
"""

# 시간초과
# for _ in range(T):
#     # 서쪽, 동쪽
#     N, M = map(int, input().split())
    
#     def comb(n, r):
#         if r == 0 or r == n:
#             return 1
#         return comb(n-1, r-1) + comb(n-1, r)
    
#     print(comb(M, N))