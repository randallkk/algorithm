# 컨베이어 벨트 위의 로봇 gold 5
# https://www.acmicpc.net/problem/20055
# python 3  34160 KB	3084 ms
# pypy3  120996 KB	1680 ms

from collections import deque


def solution():
    answer = 0
    N, K = map(int, input().split())
    belt = deque(map(int, input().split()))  # belt[idx]: 벨트의 내구도
    robots = deque()  # idx: 로봇 번호, robots[idx]: 로봇 위치
    visited = deque([-1] * 2 * N)  # visited[idx]: 방문한 로봇의 번호, 없을 시 -1
    while belt.count(0) < K:
        answer += 1
        # 1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다.
        # 벨트 회전
        belt.rotate()
        visited.rotate()

        # 2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다. 만약 이동할 수 없다면 가만히 있는다.
        idx = 0
        while idx < len(robots):
            # 로봇 회전
            robots[idx] += 1
            # 내리는 위치에 도달하면 그 즉시 내린다.
            if robots[idx] == N - 1:
                del robots[idx]
                visited[N - 1] = -1
                continue
            # 로봇 이동: 이동하려는 칸에 로봇이 없고, 내구도가 남아있으면
            if visited[robots[idx] + 1] == -1 and belt[robots[idx] + 1] > 0:
                visited[robots[idx]] = -1
                robots[idx] += 1
                belt[robots[idx]] -= 1
                visited[robots[idx]] = idx
            # 내리는 위치에 도달하면 그 즉시 내린다.
            if robots[idx] == N - 1:
                del robots[idx]
                visited[N - 1] = -1
                continue
            idx += 1

        # 3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
        if belt[0] > 0 and visited[0] == -1:
            belt[0] -= 1
            visited[0] = len(robots)
            robots.append(0)
    print(answer)


solution()
