# 색종이 만들기 silver 2
# https://www.acmicpc.net/problem/2630
import sys

input = sys.stdin.readline

white = 0
blue = 0


def cut(x1, y1, x2, y2):
    global white, blue
    if x1 == x2 and y1 == y2:
        return white, blue
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            if paper[i][j] != paper[x1][y1]:
                cut(x1, y1, x1 + (x2 - x1) // 2, y1 + (y2 - y1) // 2)
                cut(x1, y1 + (y2 - y1) // 2 + 1, x1 + (x2 - x1) // 2, y2)
                cut(x1 + (x2 - x1) // 2 + 1, y1, x2, y1 + (y2 - y1) // 2)
                cut(x1 + (x2 - x1) // 2 + 1, y1 + (y2 - y1) // 2 + 1, x2, y2)
                return False
    if paper[x1][y1]:
        blue += 1
    else:
        white += 1


n = int(input())
paper = []
for _ in range(n):
    paper.append(list(map(int, input().split())))

cut(0, 0, n - 1, n - 1)

print(white)
print(blue)
