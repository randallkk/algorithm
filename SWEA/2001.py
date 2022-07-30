# 2001. 파리 퇴치 D2
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PzOCKAigDFAUq

T = int(input())

def killFlies(x, y, m):
    dead = 0
    for i in range(x,x+m):
        for j in range(y,y+m):
            dead += arr[i][j]
    return dead

for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    maxidx = -1
    maxdead = -1

    for x in range(n-m+1):
        for y in range(n-m+1):
            maxdead = max(maxdead, killFlies(x,y,m))
    
    print("#%d %d" %(test_case, maxdead))