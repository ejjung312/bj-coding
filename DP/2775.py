import sys

input = sys.stdin.readline

"""
T - 테스트케이스
k - k층
n - n호
"""
T = int(input())

# result = []

for _ in range(T):
    k = int(input())
    n = int(input())

    # 0층
    result = [i for i in range(1, n+1)]

    # k층
    for i in range(k):
        # n호
        for j in range(1, n):
            result[j] += result[j-1]

    print(result[-1])
"""
0층 1호 => 1
0층 2호 => 2
0층 3호 => 3

a층의 b호에 살려면 a-1층의 1호부터 b호까지 사람들의 수
1층 1호 => 1
1층 2호 => 3
1층 3호 => 6

2층 1호 => 1
2층 2호 => 4
2층 3호 => 10

1층 3호 => 6명
2층 3호 => 10명

"""