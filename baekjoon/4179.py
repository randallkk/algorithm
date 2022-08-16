# 불! gold 4
# https://www.acmicpc.net/problem/4179
import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# bfs
def bfs(fire, jihoon):
    global r, c
    fireLv = len(fire)
    jihoonLv = len(jihoon)
    time = 1

    while True:
        for _ in range(fireLv):
            curFire = fire.popleft()
            for i in range(4):
                nx = curFire[0] + dx[i]
                ny = curFire[1] + dy[i]
                if nx < 0 or nx >= r or ny < 0 or ny >= c: continue
                else:
                    if maze[nx][ny] == '.' or maze[nx][ny] == 'J':
                        maze[nx][ny] = 'F'
                        fire.append((nx, ny))
        fireLv = len(fire)
        for _ in range(jihoonLv):
            curJihoon = jihoon.popleft()
            if curJihoon[0] == 0 or curJihoon[0] == r-1 \
                or curJihoon[1] == 0 or curJihoon[1] == c-1:
                return time
            for i in range(4):
                nx = curJihoon[0] + dx[i]
                ny = curJihoon[1] + dy[i]
                if nx < 0 or nx >= r or ny < 0 or ny >= c: continue
                else:
                    if maze[nx][ny] == '.':
                        maze[nx][ny] = 'J'
                        jihoon.append((nx, ny))
        jihoonLv = len(jihoon)
        time += 1
        if jihoonLv == 0: return "IMPOSSIBLE"   # 지훈이가 탈출하지 못하고 갈 곳도 없어지면 죽음

# input 받기
r, c = map(int, input().split())
maze = []
for _ in range(r):
    maze.append(list(input().rstrip()))

# queue 초기화
jihoon = deque()
fire = deque()
for i in range(r):
    for j in range(c):
        if maze[i][j] == 'J':
            jihoon.append((i,j))
        if maze[i][j] == 'F':
            fire.append((i,j))
print(bfs(fire, jihoon))
