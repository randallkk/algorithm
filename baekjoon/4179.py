# 불! gold 4
# https://www.acmicpc.net/problem/4179
import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(jihoon, fire):
    que = deque()
    fires = deque()
    que.append(jihoon)
    maze[jihoon[0]][jihoon[1]] = 0
    fires.append(fire)
    while que:
        jihoon = que.popleft()
        fire = fires.popleft()
        for i in range(4):
            nx = jihoon[0] + dx[i]  # 지훈이 이동경로 (지훈이가 이동한 횟수 기록)
            ny = jihoon[1] + dy[i]
            if nx == 0 or nx == r - 1 or ny == 0 or ny == c - 1:  # 지훈이가 가장자리면 탈출
                if maze[nx][ny] != "#":
                    print(maze[jihoon[0]][jihoon[1]] + 2)
                    return True
            elif 0 < nx < r - 1 and 0 < ny < c - 1:  # 지훈이가 가장자리 아니고 안쪽이면
                if maze[nx][ny] == ".":
                    maze[nx][ny] = maze[jihoon[0]][jihoon[1]] + 1
                    que.append((nx, ny))
            if level != maze[nx][ny]:
                while fires:
                    nx = fire[0] + dx[i]  # 불 이동경로 ("F" 기록)
                    ny = fire[1] + dy[i]
                    if 0 <= nx < r and 0 <= ny < c:
                        if maze[nx][ny] != "#" and maze[nx][ny] != "F":
                            maze[nx][ny] = "F"
                            fires.append((nx, ny))
    print("IMPOSSIBLE")
    return False


r, c = map(int, input().split())
maze = []  # graph
jihoon = False
fire = False
for _ in range(r):
    row = list(input().rstrip())
    maze.append(row)
    if not jihoon and "J" in row:
        jihoon = (len(maze) - 1, row.index("J"))  # jihoon의 x좌표, y좌표
    if not fire and "F" in row:
        fire = (len(maze) - 1, row.index("F"), 0)  # fire의 x좌표, y좌표, level(= 지훈이가 이동한 횟수)
bfs(jihoon, fire)
