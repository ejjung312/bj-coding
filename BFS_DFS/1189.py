"""
실버 1
"""
import sys

input = sys.stdin.readline

R, C, K = map(int,input().split())

graph=[ list(input().strip()) for i in range(R) ]
chk = [[False] * (C) for _ in range(R)]

d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

answer=0
def DFS(x, y, dist):
    global R, C, K, graph, d, answer, chk
    
    chk[x][y] = True
    
    if dist > K:
        chk[x][y] = False
        return

    if graph[x][y] == 'T':
        return
    
    if x == 0 and y == C-1:
        if dist == K:
            answer += 1
        chk[x][y] = False
        return

    for dx, dy in d:
        nx, ny = x + dx, y + dy
        if 0 <= nx < R and 0 <= ny < C:
            if not chk[nx][ny]:
                DFS(nx, ny, dist+1)
    chk[x][y] = False

DFS(R-1,0,1)
print(answer)