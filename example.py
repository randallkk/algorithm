def inputprac():
    a = input()
    b = input().split()  # str을 white space 단위로 자름
    c, d = map(int, input().split())  # list의 str을 각각 int로 변환해 줌
    e = list(
        map(lambda x: int(x) + 2, input().split()))  # input으로 받은 list(str) > 각각을 int로 바꾸고 2를 더함  > map object를 list로 변환

    print(a, b, c, d, e)


'''a = "Elsa"
b = "Elsa"
c = a
d = []
e = []
f = d

#string
print(id(a))
print(id(b))
print(id(c))
#iterables
print(id(d))
print(id(e))
print(id(f))

if a == b:
    print("a와 b는 같은 값(value)을 가집니다.")
if b == c:
    print("b와 c는 같은 값(value)을 가집니다.")
if c == a:
    print("c와 a는 같은 값(value)을 가집니다.")
if d == e:
    print("d와 e는 같은 값(value)을 가집니다.")
if e == f:
    print("e와 f는 같은 값(value)을 가집니다.")
if f == d:
    print("f와 d는 같은 값(value)을 가집니다.")

if a is b:
    print("a와 b는 같은 객체(Object)를 참조합니다.") 
if b is c:
    print("b와 c는 같은 객체(Object)를 참조합니다.")
if c is a:
    print("c와 a는 같은 객체(Object)를 참조합니다.")
if d is e:
    print("d와 e는 같은 객체(Object)를 참조합니다.") 
if e is f:
    print("e와 f는 같은 객체(Object)를 참조합니다.")
if f is d:
    print("f와 d는 같은 객체(Object)를 참조합니다.")'''

from pprint import pprint
from pip import main


def initialize():
    i, j = map(int, input().split())
    a = []
    for _ in range(j):
        lst = []
        for _ in range(i):
            lst.append(0)
        a.append(lst)
    b = [[0 for _ in range(i)] for _ in range(j)]
    print(a)
    print(b)


def showGraphs(edges, n):  # edges = [[node1, node2, cost], ... ] / n : node 수
    INF = 999999
    # adjMat = [[cost for _ in ]]
    adjMat = [[INF for _ in range(n + 1)] for _ in range(n)]
    adjMat.insert(0, [])
    adjLst = [[] for _ in range(n + 1)]

    for i in range(n):
        adjMat[i + 1][i + 1] = 0
    for edge in edges:
        adjMat[edge[0]][edge[1]] = edge[2]
        adjMat[edge[1]][edge[0]] = edge[2]

    for edge in edges:
        adjLst[edge[0]].append((edge[1], edge[2]))
        adjLst[edge[1]].append((edge[0], edge[2]))

    print("~~ Adjacency Matrix ~~")
    pprint(adjMat)
    print("\n")
    print("~~ Adjacency List ~~")
    pprint(adjLst)
    print("\n")
    print("~~ Graph(set of Edges) ~~")
    pprint(edges)


'''원시적인 BFS'''


def bfs1(graph, root):
    queue = []  # queue: 차례로 방문할 노드들
    visited = []  # visited: 방문한 노드들

    queue.append(root)
    visited.append(root)
    print("queue:", queue)
    while queue:  # queue에 있는 노드에 대해
        node = queue.pop(0)
        print("***** node:", node, "*****")
        for line in graph:  # graph의 간선(line) 중에서
            if node in line:  # 노드를 포함하는 line이 있으면
                for dot in line:
                    if not dot == node:  # 그 노드와 연결된 다른 노드를
                        if not dot in visited:  # 방문한 적 있는지 검사한 다음에
                            visited.append(dot)  # 없으면 방문자 리스트에 올리고
                            queue.append(dot)  # queue에도 넣자.
        print("queue:", queue)
        print("visited:", visited)


'''visited를 boolean list로 만들고, deque를 사용한 BFS'''


def bfs2(graph, root):
    queue = deque([root])  # queue: 차례로 방문할 노드들
    visited = [False] * (len(graph) + 1)  # visited: 노드들 방문 이력
    visited[root] = True

    print("queue:", queue)

    while queue:  # queue에 있는 노드에 대해
        node = queue.popleft()
        print("***** node:", node, "*****")
        for line in graph:  # graph의 간선(line) 중에서
            if node in line:  # 노드를 포함하는 line이 있으면
                for dot in line:
                    if dot != node and not visited[dot]:  # 그 노드와 연결된 다른 노드를 방문한 적 있는지 검사한 다음에
                        visited[dot] = True  # 없으면 방문자 리스트에 올리고
                        queue.append(dot)  # queue에도 넣자.
        print("queue:", queue)
        print("visited:", visited)


'''간선을 소거하는 BFS'''


def bfs3(graph, root):
    edges = deque(graph)  # edges: 간선들의 모임
    queue = deque([root])  # queue: 차례로 방문할 노드들
    visited = [False] * (len(graph) + 1)  # visited: 노드들 방문 이력
    visited[root] = True

    print("queue:", queue)

    while queue:  # queue에 있는 노드에 대해
        node = queue.popleft()
        print("***** node:", node, "*****")
        for line in edges:  # graph의 간선(line) 중에서
            if node in line:  # 노드를 포함하는 line이 있으면
                for dot in line:
                    if dot != node and not visited[dot]:  # 그 노드와 연결된 다른 노드를 방문한 적 있는지 검사한 다음에
                        visited[dot] = True  # 없으면 방문자 리스트에 올리고
                        queue.append(dot)  # queue에도 넣자.
        print("queue:", queue)
        print("visited:", visited)


# deque 라이브러리 불러오기
from collections import deque


# BFS 메서드 정의
def bfs(graph, node, visited):
    # 큐 구현을 위한 deque 라이브러리 활용
    queue = deque([node])
    # 현재 노드를 방문 처리 
    visited[node] = True

    # 큐가 완전히 빌 때까지 반복
    while queue:
        # 큐에 삽입된 순서대로 노드 하나 꺼내기
        v = queue.popleft()
        # 탐색 순서 출력
        print(v, end=' ')
        # 현재 처리 중인 노드에서 방문하지 않은 인접 노드를 모두 큐에 삽입
        for i in graph[v]:
            if not (visited[i]):
                queue.append(i)
                visited[i] = True
    return 0


if __name__ == "__main__":
    stringlist = ["3", "2", "1", "4"]
    intList = [3, 2, 1, 4]
    stringlist.sort()
    intList.sort()
    print(stringlist)
    print(intList)
