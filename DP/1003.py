"""
실버 3
"""

import sys

input = sys.stdin.readline

T = int(input())

"""
        0   1
fibo(0) 1   0 
fibo(1) 0   1
fibo(2) 1   1
fibo(3) 1   2
fibo(4) 2   3

0 -> fibo(n-2)의 0 출력 횟수 + fibo(n-1)의 0 출력 횟수
1 -> fibo(n-2)의 1 출력 횟수 + fibo(n-1)의 1 출력 횟수
"""

for _ in range(T):
    N = int(input())
    
    cnt_0 = [1, 0]
    cnt_1 = [0, 1]
    
    for i in range(N-1):
        cnt_0.append(cnt_0[-1]+cnt_0[-2])
        cnt_1.append(cnt_1[-2]+cnt_1[-1])
    
    print(cnt_0)
    print(cnt_1)
    
    # print(cnt_0[N], cnt_1[N])