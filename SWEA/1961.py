import math

T = int(input())
def rotate(arr):
    n = len(arr)
    answer = [[0]*n for _ in range(n)]
    for k in range(math.ceil(n/2+1)):
        lefttop = arr[k][k]
        righttop = arr[k][n-k-1]
        leftbottom = arr[n-k-1][k]
        rightbottom = arr[n-k-1][n-k-1]

        answer[k][k] = leftbottom
        answer[k][n-k-1] = lefttop
        answer[n-k-1][k] = rightbottom
        answer[n-k-1][n-k-1] = righttop

        top = arr[k][k+1:n-k-1]
        bottom = arr[n-k-1][k+1:n-k-1]
        left = [arr[k+i+1][k] for i in range(n-2*k-2)]
        right = [arr[k+i+1][n-k-1] for i in range(n-2*k-2)]

        for i in range(k+1,n-k-1):
            answer[k][i] = left[-i+k]
        for i in range(k+1,n-k-1):
            answer[n-k-1][i] = right[-i+k]
        for i in range(n-2*k-2):
            answer[k+1+i][k] = bottom[i]
        for i in range(n-2*k-2-1,-1,-1):
            answer[k+1+i][n-k-1] = top[i]
    return answer


for test_case in range(1, T + 1):
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))
    arr90 = rotate(arr)
    arr180 = rotate(arr90)
    arr270 = rotate(arr180)
    print("#%d" %(test_case))
    for i in range(n):
        print(''.join(map(str, arr90[i])), ''.join(map(str,arr180[i])), ''.join(map(str,arr270[i])))
