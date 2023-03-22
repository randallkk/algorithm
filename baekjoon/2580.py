# 스도쿠 gold 4
# https://www.acmicpc.net/problem/2580

hori = [[False] * 10 for _ in range(10)]
vert = [[False] * 10 for _ in range(10)]
sqr = [[False] * 10 for _ in range(10)]

sedoku = [[-1]*10]
blank = []

def fill(cnt):
    if cnt == len(blank):
        for i in range(1,10):   
            print(' '.join(map(str, sedoku[i][1:])))
        exit(0)
    r = blank[cnt][0]
    c = blank[cnt][1]
    for i in range(1,10):
        if hori[r][i] == True: continue
        if vert[c][i] == True: continue
        if sqr[(r-1)//3*3 + (c-1)//3 + 1][i] == True: continue
        sedoku[r][c] = i
        hori[r][i] = True
        vert[c][i] = True
        sqr[(r-1)//3*3 + (c-1)//3 + 1][i] = True
        fill(cnt+1)
        hori[r][i] = False
        vert[c][i] = False
        sqr[(r-1)//3*3 + (c-1)//3 + 1][i] = False


# input 처리
for _ in range(9):
    l = [-1]
    l.extend(list(map(int, input().split())))
    sedoku.append(l)
for i in range(1, 10):
    for j in range(1, 10):
        if sedoku[i][j] == 0:
            blank.append((i, j))
        else:
            hori[i][sedoku[i][j]] = True
            vert[j][sedoku[i][j]] = True
            sqr[(i-1)//3*3 + (j-1)//3 + 1][sedoku[i][j]] = True

fill(0)