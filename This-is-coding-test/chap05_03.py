from collections import deque


def bfs(frame, start, visited):
    x = start[0]
    y = start[1]
    try:
        if not frame[x][y + 1]:
            queue.append((x, y + 1))
    except IndexError:
        pass
    try:
        if not frame[x + 1][y]:
            queue.append((x + 1, y))
    except IndexError:
        pass
    if len(queue) == 0:
        return 1
    try:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            bfs(frame, node, visited)
    except IndexError:
        pass


if __name__ == '__main__':
    answer = 0
    frame = []
    n, m = map(int, input().split())
    for _ in range(n):
        frame.append(list(map(int, input())))

    visited = []
    queue = deque()
    for i in range(n * m):
        if frame[i] not in visited:
            answer += bfs(frame, frame[i], visited)

    print(answer)
