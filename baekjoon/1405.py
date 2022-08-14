# 미친 로봇 gold 5
# https://www.acmicpc.net/problem/1405

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
n, *probability = map(int, input().split())
probability = [prob/100 for prob in probability]
visited = [[False]*(n*2+1) for _ in range(n*2+1)]

answer = 0
def dfs(x, y, dist, prob):
    if dist == 0:
        global answer
        answer += prob
        return
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n*2+1 or ny < 0 or ny >= n*2+1: continue
        else:
            if not visited[nx][ny]:
                dfs(nx, ny, dist-1, prob*probability[i])
    visited[x][y] = False

visited[n][n]
dfs(n, n, n, 1)
print(answer)