"""
실버 3
"""
import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    x1, y1, x2, y2 = map(int, input().split()) # 출발점, 도착점
    n = int(input()) # 행성 개수
    
    cnt = 0
    for _ in range(n):
        cx, cy, r = map(int, input().split()) # 행성 중심점, 반지름
        
        # 진입의 경우 -> 원의 내부에 존재
        # 이탈의 경우 -> 원의 외부에 존재
        start = (((x1 - cx) ** 2) + ((y1 - cy) ** 2)) ** 0.5 #행성중심부터 시작점까지의 거리
        end = (((cx - x2) ** 2) + ((cy - y2) ** 2)) ** 0.5 #행성중심부터 도착점까지의 거리

        if start < r and end < r: #시작점과 도착점 모두 원 안에 있을 경우
            pass
        elif start < r: #시작점이 안에 있을 경우
            cnt += 1
        elif end < r: #도착점이 안에 있을 경우
            cnt += 1
    
    print(cnt)