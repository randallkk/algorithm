# 욕심쟁이 판다 gold 3
# https://www.acmicpc.net/problem/1937
import sys
sys.setrecursionlimit(12500000)

n = int(input())
forest = []
visited = [[1]*n for _ in range(n)]
maxMove = 0
for _ in range(n):
    forest.append(list(map(int, input().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def move(x, y):
    global maxMove
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        else:
            if(forest[nx][ny] > forest[x][y]):
                if visited[nx][ny] == 1:
                    move(nx, ny)
                visited[x][y] = max(visited[x][y], visited[nx][ny] + 1)
    maxMove = max(maxMove, visited[x][y])


for i in range(n):
    for j in range(n):
        if visited[i][j] == 1:
            move(i, j)
print(maxMove)