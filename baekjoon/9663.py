# N-Queen gold 4
# https://www.acmicpc.net/problem/9663

answer = 0
n = int(input())
board = [[True] * n for _ in range(n)]  # False랑 0으로 둘 다 풀어보기


def placeQueen(board, num):
    global answer
    if not num:
        answer += 1
        return
    for j in range(n):
        if board[n - num][j]:
            for i in range(n - num + 1, n):
                board[i][j] = False
                if 0 <= j - (i - n + num) < n:
                    board[i][j - (i - n + num)] = False
                if 0 <= j + (i - n + num) < n:
                    board[i][j + (i - n + num)] = False
            placeQueen(board[:], num - 1)
    return


placeQueen(board, n)
print(answer)