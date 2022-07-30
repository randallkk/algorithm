# 1974. 스도쿠 검증 D2
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5Psz16AYEDFAUq

T = int(input())

for test_case in range(1, T + 1):
    board = [list(map(int, input().split())) for _ in range(9)]
    flag = 1
    for i in range(9):
        block = set(board[i])
        if len(block) != 9:
            flag = 0
            break
        block = set()
        for j in range(9):
            block.add(board[j][i])
        if len(block) != 9:
            flag = 0
            break
    for i in range(0,9,3):
        for j in range(0,9,3):
            block = set(board[i][j:j+3])|set(board[i+1][j:j+3])|set(board[i+2][j:j+3])
            if len(block) != 9:
                flag = 0
                break
    print("#%d %d" %(test_case,flag))
    