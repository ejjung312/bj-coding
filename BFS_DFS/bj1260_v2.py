"""
BFS - 큐
DFS - 스택,재귀
"""

N, M, V = map(int, input().split())
graph = [[0]*(N+1) for _ in range(N+1)]

for i in range (M):
    a,b = map(int,input().split())
    graph[a][b] = graph[b][a] = 1 # 연결되어있음
    
def dfs(V):
    visited_dfs[V] = 1
    result_dfs.append(V)
    for i in range(1, N+1):
        if graph[V][i] == 1 and visited_dfs[i] == False:
            dfs(i)

def bfs(V):
    queue = [V]
    visited_bfs[V] = True
    while queue:
        V = queue.pop(0)
        result_bfs.append(V)
        for i in range(1, N+1):
            if visited_bfs[i] == False and graph[V][i] == 1:
                queue.append(i)
                visited_bfs[i] = True


visited_bfs = [False] * (N+1)
visited_dfs = visited_bfs.copy()

result_bfs = []
result_dfs = []

dfs(V)
bfs(V)

print(result_dfs)
print(result_bfs)
