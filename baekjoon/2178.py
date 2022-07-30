# 미로 탐색 silver 1
# https://www.acmicpc.net/problem/2178
import sys
from collections import deque


def bfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    que = deque([(x, y)])
    graph[x][y] = 1
    while que:
        x, y = que.popleft()
        if x == n-1 and y == m-1:
            print(graph[x][y])
            return True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == "1":
                graph[nx][ny] = graph[x][y] + 1
                que.append((nx, ny))


input = sys.stdin.readline
n, m = map(int, input().split())
graph = []
for _ in range(n):
    row = list(input().rstrip())
    graph.append(row)
bfs(0, 0)