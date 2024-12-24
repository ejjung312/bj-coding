import sys

input = sys.stdin.readline

"""
높이 구하기 h (1<=h<=N)
N: 굴다리 길이
M: 가로등 개수
x: 가로등 위치 (0<=x<=N)
"""

N = int(input())
M = int(input())
x_list = list(map(int, input().split()))

start, end = 1, N
min_height = 0

def checkLight(height):
    prev = 0
    for x in x_list:
        if x - height > prev:
            return False
        else:
            prev = x + height
    return prev >= N
    

while start <= end:
    mid = (start + end) // 2
    
    if checkLight(mid):
        end = mid - 1
        min_height = mid
    else:
        start = mid + 1

print(min_height)