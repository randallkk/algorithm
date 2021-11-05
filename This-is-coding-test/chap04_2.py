def solve():
    dx = [2, 1]
    dy = [1, 2]
    direction = [1, -1]
    row, col = input()
    x = ord(row) - ord('a')
    y = int(col) - 1
    answer = 0
    for i in range(2):
        for d in direction:
            nx = x + dx[i] * d
            ny = y + dy[i] * d
            if nx < 0 or nx >= 8 or ny < 0 or ny >= 8:
                pass
            else:
                answer += 1
    print(answer)

if __name__ == "__main__":
    solve()