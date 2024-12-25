import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
S = 0

for i in range(N):
    S += min(A) * max(B)
    A.pop(A.index(min(A)))
    B.pop(B.index(max(B)))

print(S)

"""
18
B : 2 7 8 3 1
A : 1 1 1 6 0

B': 1 2 3 7 8
A': 6 1 1 1 0

6 2 3 7 0 => 18 

2 7 0 3 6 => 18
--------------

80
B : 10 30 20
A : 1 1 3

B': 10 20 30
A': 3 1 1

30 20 30 = 80

--------------

A: 5 15 100 31 39 0 0 3 26
B: 11 12 13 2 3 4 5 9 1

A': 100 39 31 26 15 5 3 0 0
B':  1  2  3  4  5  9 11 12 13
    100 78 93 104 75 45 33 0 0 
"""