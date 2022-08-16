# 숨바꼭질2 gold 4
# https://www.acmicpc.net/problem/12851

from collections import deque


n, k = map(int, input().split())        # n: 수빈이 위치, k: 동생 위치
visited = [False] * 100001
time = 0
queue = deque()

if n != k:
    queue.append(n)
    visited[n] = True
    fastest = -1
    route = 0
    size = len(queue)
else:
    print(0)
    print(1)
while queue:
    cur = queue.popleft()
    visited[cur] = True
    size -= 1
    children = [cur + 1, cur - 1, cur * 2]

    for next in children:
        if next < 0 or next > 100000: continue      # 경계 조건 (0 ≤ N ≤ 100,000)
        if next == k:
            if fastest == -1:
                fastest = time + 1
            route += 1
        if not visited[next]:       # 나중에 도착한 경우는 최단 시간이 아니다.
            queue.append(next)

    if size == 0:           # 한 level이 끝나면
        if fastest != -1:   # 수빈이가 동생을 잡았는지 검사
            print(fastest)
            print(route)
            break
        size = len(queue)   # 다음 level 시작
        time += 1
