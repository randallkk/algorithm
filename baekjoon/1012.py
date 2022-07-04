# 유기농 배추 silver 2
# https://www.acmicpc.net/problem/1012
import sys

sys.setrecursionlimit(10**7)
def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    if field[x][y]:
        field[x][y] = 0
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False


for _ in range(int(input())):
    answer = 0
    m, n, k = map(int, input().split())
    field = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        y, x = map(int, input().split())
        field[x][y] = 1
    for i in range(n):
        for j in range(m):
            if dfs(i, j):
                answer += 1
    print(answer)