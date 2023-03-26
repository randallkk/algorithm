# 코드트리 빵
# https://www.codetree.ai/training-field/frequent-problems/codetree-mon-bread


from collections import deque


def solution():
    answer = 0
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    dr = [0, 0, 1, -1]
    dc = [-1, 1, 0, 0]

    def bfs(x: int, y: int):
        que = deque([(x, y)])
        visited = [[n * n] * n for _ in range(n)]
        visited[x][y] = 0
        dist = n * n
        store = (n, n)
        arrived = False
        while que:
            num = len(que)
            for _ in range(num):
                r, c = que.popleft()
                for i in range(4):
                    nr = r + dr[i]
                    nc = c + dc[i]
                    if (
                        nr < 0
                        or nr >= n
                        or nc < 0
                        or nc >= n
                        or grid[nr][nc] == 2  # 다른 사람이 방문한 베이스캠프나 편의점일 경우
                        or visited[nr][nc] < visited[r][c] + 1  # 더 짧은 거리로 방문했을 경우
                    ):
                        continue
                    if grid[nr][nc] == 1:  # 베이스 캠프면
                        arrived = True
                        if store[0] > nr:
                            store = (nr, nc)
                        elif store[0] == nr and store[1] > nc:
                            store = (nr, nc)
                    que.append((nr, nc))
                    visited[nr][nc] = min(visited[nr][nc], visited[r][c] + 1)
            if arrived:
                grid[store[0]][store[1]] = 2
                grid[x][y] = 2
                return visited[store[0]][store[1]]
        return visited[store[0]][store[1]]

    for person in range(1, m + 1):
        x, y = map(int, input().split())
        dist = bfs(x - 1, y - 1)
        answer = max(answer, person + dist)
    print(answer)


solution()
