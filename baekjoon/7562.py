# 나이트의 이동 silver 1
# https://www.acmicpc.net/problem/7562

import sys
from collections import deque


def dfs(x, y):
    if x < 0 or x >= i or y < 0 or y >= i:
        return False
    if not board[x][y]:
        board[x][y] = 1
        dfs(x - 2, y - 1)
        dfs(x - 2, y + 1)
        dfs(x - 1, y - 2)
        dfs(x - 1, y + 2)
        dfs(x + 1, y - 2)
        dfs(x + 1, y + 2)
        dfs(x + 2, y - 1)
        dfs(x + 2, y + 1)
        return True
    return False



'''
def bfs(x, y):
    que = deque([(x, y)])
    dx = [-2, -2, -1, -1, 1, 1, 2, 2]
    dy = [-1, 1, -2, 2, -2, 2, -1, 1]
    board[x][y] = 1
    while que:
        x, y = que.popleft()
        if x == target[0] and y == target[1]:
            print(board[x][y]-1)
            return True
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= I or ny < 0 or ny >= I:
                continue
            if nx == target[0] and ny == target[1]:
                print(board[x][y])
                return True
            if not board[nx][ny]:
                que.append((nx, ny))
                board[nx][ny] = board[x][y] + 1


for _ in range(int(input())):
    I = int(input())
    board = [[0] * I for _ in range(I)]
    start = list(map(int, input().split()))
    target = list(map(int, input().split()))
    bfs(start[0], start[1])
'''