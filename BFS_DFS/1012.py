"""
실버 2
RecursionError
"""
import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

T = int(input())

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

for _ in range(T):
    M, N, K = map(int, input().split())
    
    graph = [[0] * (M) for _ in range(N)]
    chk = [[False] * (M) for _ in range(N)]
    for _ in range(K):
        X, Y = map(int, input().split())
        graph[Y][X] = 1
    
    cnt = 0
    result = []
    def bfs(cy, cx):
        global cnt
        cnt += 1
        
        for k in range(4):
            ny = dy[k] + cy
            nx = dx[k] + cx
        
            if 0<=ny<N and 0<=nx<M:
                if graph[ny][nx] == 1 and chk[ny][nx] == False:
                    chk[ny][nx] = True
                    bfs(ny, nx)
    
    for y in range(N):
        for x in range(M):
            if graph[y][x] == 1 and chk[y][x] == False:
                chk[y][x] = True
                cnt = 0
                bfs(y, x)
                result.append(cnt)
    
    print(len(result))