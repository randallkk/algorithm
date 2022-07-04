def solution(numbers, target):
    answer = 0

    def dfs(idx, operated, target):
        nonlocal answer
        if idx < len(numbers):
            number = numbers[idx]
            dfs(idx+1, operated + number, target)
            dfs(idx+1, operated - number, target)
            return
        else:
            if operated == target:
                answer += 1

    dfs(0, 0, target)
    return answer


print(solution([1, 1, 1, 1, 1], 3))
