# 1959. 두 개의 숫자열 D2
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PpoFaAS4DFAUq&categoryId=AV5PpoFaAS4DFAUq&categoryType=CODE&problemTitle=1959


def solve(n, m, arr1, arr2):
    answer = 0
    if n > m:
        for i in range(n - m + 1):
            answer = max(answer, sum(map(lambda j: arr1[i + j] * arr2[j], range(m))))
    elif n < m:
        for i in range(m - n + 1):
            answer = max(answer, sum(map(lambda j: arr1[j] * arr2[i + j], range(n))))
    else:
        for i in range(n):
            answer += arr1[i] * arr2[i]
    return answer


t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print("#%d" %(i + 1), solve(n, m, a, b))
