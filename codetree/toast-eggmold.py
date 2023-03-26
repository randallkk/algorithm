# 토스트 계란틀
# https://www.codetree.ai/training-field/frequent-problems/toast-eggmold


from collections import deque


def solution():
    answer = 0
    n, L, R = map(int, input().split())
    frame = [list(map(int, input().split())) for _ in range(n)]
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    moved = True
    while moved:
        visited = [[False] * n for _ in range(n)]
        moved = False
        for i in range(n):
            for j in range(n):
                if visited[i][j]:
                    continue
                eggs = set()
                egg_amount = frame[i][j]
                que = deque([(i, j)])
                visited[i][j] = True
                while que:
                    r, c = que.popleft()
                    for k in range(4):
                        nr = r + dr[k]
                        nc = c + dc[k]
                        if (
                            nr < 0
                            or nr >= n
                            or nc < 0
                            or nc >= n
                            or visited[nr][nc]
                            or abs(frame[r][c] - frame[nr][nc]) < L
                            or abs(frame[r][c] - frame[nr][nc]) > R
                        ):
                            continue
                        que.append((nr, nc))
                        eggs.add((nr, nc))
                        egg_amount += frame[nr][nc]
                        visited[nr][nc] = True
                if eggs:
                    eggs.add((i, j))
                    moved = True
                    egg_amount //= len(eggs)
                for r, c in eggs:
                    frame[r][c] = egg_amount
        if moved:
            answer += 1
    print(answer)


solution()
