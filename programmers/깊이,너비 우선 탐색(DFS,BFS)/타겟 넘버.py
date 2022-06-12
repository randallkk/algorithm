def solution(numbers, target):
    answer = 0
    answer = dfs(numbers, 0, target, answer)
    return answer


def dfs(numbers, operated, target, answer):
    if numbers:
        number = numbers.pop(0)
        print("numbers:", numbers, "/ operated:", operated, "/ number:", number, "/ answer:", answer)
        answer += dfs(numbers, operated + number, target, answer)
        numbers.insert(0, number)
        print("numbers:", numbers, "/ operated:", operated, "/ number:", number, "/ answer:", answer)
        answer += dfs(numbers, operated - number, target, answer)
        return answer
    else:
        if operated == target:
            print("edge")
            return answer + 1
        else:
            print("operated != target:", operated)
            return answer


print(solution([4, 1, 2, 1], 4))
