# 행렬의 곱셈 level 2
# https://school.programmers.co.kr/learn/courses/30/lessons/12949

def solution(arr1, arr2):
    n = len(arr1)
    k = len(arr2)
    m = len(arr2[0])
    answer = [[0]*m for _ in range(n)]
    for row in range(n):
        for col in range(m):
            for i in range(k):
                answer[row][col] += arr1[row][i] * arr2[i][col]
    return answer