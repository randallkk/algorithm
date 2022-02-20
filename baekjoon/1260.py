# DFS와 BFS silver 2
# https://www.acmicpc.net/problem/1260

from collections import deque


def dfs(n, graph, v):
    visited = [False] * (n + 1)
    stack = []
    route = []

    return route
def bfs(n, graph, v):
    visited = [False] * (n + 1)
    queue = deque([])
    route = []

    queue.append(v)
    while queue:
        p = queue.popleft() # pointer
        route.append(route)
        for edge in graph:
            try:
                edge.remove(p)
                node = edge.pop(0)
                if not visited[node]:
                    queue.append(node)
                    visited[node] = True
            except ValueError:
                pass

    return route

if __name__ == '__main__':
    n, m, v = map(int, input().split()) # 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V
    graph = [list(map(int, input().split())) for _ in range(m)] # 간선이 연결하는 두 정점의 번호

    # print(dfs(n, graph, v))
    print(bfs(n, graph, v))