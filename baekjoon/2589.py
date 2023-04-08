# 보물섬 gold 5
# https://www.acmicpc.net/problem/2589

from collections import deque
import sys
from typing import List


def bfs(i: int, j: int, board: List[List[int]]):
    N = len(board)
    M = len(board[0])
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    maxdist = 0
    visited = [[0] * M for _ in range(N)]
    que = deque()
    que.append((i, j))
    visited[i][j] = 1
    while que:
        r, c = que.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if (
                nr < 0
                or nr >= N
                or nc < 0
                or nc >= M
                or board[nr][nc] == "W"
                or visited[nr][nc]
            ):
                continue
            que.append((nr, nc))
            visited[nr][nc] = visited[r][c] + 1
            maxdist = max(maxdist, visited[nr][nc])
    return maxdist - 1


def solution():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    board = [list(input()) for _ in range(N)]
    maxdist = 0
    for i in range(N):
        for j in range(M):
            if (
                board[i][j] == "W"
                or (
                    1 <= i < N - 1 and board[i + 1][j] == "L" and board[i - 1][j] == "L"
                )
                or (
                    1 <= j < M - 1 and board[i][j + 1] == "L" and board[i][j - 1] == "L"
                )
            ):
                continue
            maxdist = max(maxdist, bfs(i, j, board))
    print(maxdist)


solution()
