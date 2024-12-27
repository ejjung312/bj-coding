"""
실버 3
"""
import sys
import math

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = list(map(int, input().split()))
    
    dis = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    
    if dis == 0: # 두 원의 중심이 같을 경우 (같거나 동심원)
        if r1 == r2: # 겹칠 때
            print(-1)
        else:
            print(0)
    else: # 두 원의 중심이 다름
        if r1+r2 == dis or abs(r2-r1) == dis: # 외접 or 내접
            print(1)
        elif ((abs(r1-r2) < dis) and (dis < r1+r2)): # r1-r2 < d < r1+r2
            print(2)
        else:
            print(0)