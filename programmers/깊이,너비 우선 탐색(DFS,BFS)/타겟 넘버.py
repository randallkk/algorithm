def solution(numbers, target):
    answer = 0

    def dfs(idx, operated):
        nonlocal answer
        if idx < len(numbers):
            number = numbers[idx]
            dfs(idx+1, operated + number)
            dfs(idx+1, operated - number)
            return
        else:
            if operated == target:
                answer += 1

    dfs(0, 0)
    return answer


print(solution([1, 1, 1, 1, 1], 3))
