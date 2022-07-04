# 쿼드트리 silver 1
# https://www.acmicpc.net/problem/1992
import sys

answer = ""
input = sys.stdin.readline


def zipImg(n, x, y):
    global answer
    if not n:
        answer += ")"
        return 0
    for i in range(x, x + n):
        for j in range(y, y + n):
            if image[x][y] != image[i][j]:
                answer += "("
                half = n // 2
                zipImg(half, x, y)
                zipImg(half, x, y + half)
                zipImg(half, x + half, y)
                zipImg(half, x + half, y + half)
                answer += ")"
                return False
    answer += image[x][y]


n = int(input())
image = [list(input().rstrip()) for _ in range(n)]
zipImg(n, 0, 0)
print(answer)
