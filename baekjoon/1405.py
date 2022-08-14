# 미친 로봇 gold 5
# https://www.acmicpc.net/problem/1405

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
n, *probability = map(int, input().split())
probability = [prob/100 for prob in probability]
visited = [[False]*(n*2+1) for _ in range(n*2+1)]

answer = 0
def dfs(x, y, dist, prob):      # 현재의 x,y 좌표, 앞으로 갈 수 있는 거리, 현재 위치에 도달할 확률
    if dist == 0:           # 더 못가면
        global answer
        answer += prob      # 현재 위치에 올 확률을 더한다.
        return
    visited[x][y] = True    # 방문 처리
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n*2+1 or ny < 0 or ny >= n*2+1: continue
        else:
            if not visited[nx][ny]:     # 이전에 가지 않았던 길만 선택
                dfs(nx, ny, dist-1, prob*probability[i])    # 갈 수 있는 거리 - 1, 현재 위치에 도달할 확률 * 다음 방향을 선택할 확률
    visited[x][y] = False   # sibling의 자식node들에서 방문할 수 있게 방문 처리 해제

dfs(n, n, n, 1)
print(answer)