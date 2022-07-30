# N과 M (9) silver 2
# https://www.acmicpc.net/problem/15663

sequences = set()
n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
visited = [False] * n


def dfs(subarr, n, m):
    global sequences
    if len(subarr) == m:
        sequences.add(' '.join(map(str, subarr)))
        return
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            subarr.append(arr[i])
            dfs(subarr, n, m)
            visited[i] = False
            subarr.pop()


subarr = []
dfs([], n, m)
sq = sorted(list(sequences))
for seq in sq:
    print(seq)