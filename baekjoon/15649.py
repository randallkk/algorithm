# N과 M (1) silver 3
# https://www.acmicpc.net/problem/15649

n, m = map(int, input().split())


def choose(arr, n, m):
    if len(arr) == m:
        return arr

