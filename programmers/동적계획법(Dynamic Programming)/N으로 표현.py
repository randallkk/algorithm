# N으로 표현 level 3
# https://school.programmers.co.kr/learn/courses/30/lessons/42895

def solution(N, number):
    answer = 0

    # 자릿수 구하기
    n = number
    digit = 1
    while n < 10:
        n //= 10
        digit += 1

    dp = [0]*pow(digit, 10)
    solution(N, number-n)
    return answer

print(solution(5, 12))