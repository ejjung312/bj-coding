"""
BFS -> Queue
"""

# import sys

N = int(input())
graph = [list(map(int, input())) for _ in range(N)]
chk = [[False] * N for _ in range(N)]

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

cnt = 0
result = []
def bfs(cy, cx):
    global cnt
    cnt += 1
    
    for k in range(4):
        ny = dy[k] + cy
        nx = dx[k] + cx
        
        if 0<=ny<N and 0<=nx<N:
            if graph[ny][nx] == 1 and chk[ny][nx] == False:
                chk[ny][nx] = True
                bfs(ny, nx)
    

for y in range(N):
    for x in range(N):
        if graph[y][x] == 1 and chk[y][x] == False:
            chk[y][x] = True # 방문체크
            cnt = 0
            bfs(y, x)
            result.append(cnt)

result.sort()
print(len(result))
for i in result:
    print(i)