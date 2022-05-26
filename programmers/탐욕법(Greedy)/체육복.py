def solution(n, lost, reserve):
    answer = 0
    reservebutlost = set(lost) & set(reserve)
    lost = list(set(lost)-reservebutlost)
    reserve = list(set(reserve)-reservebutlost)
    lend = []
    for student_num in lost:
        if (student_num - 1) in reserve:
            lend.append(student_num)
            reserve.remove(student_num - 1)
        elif (student_num + 1) in reserve:
            lend.append(student_num)
            reserve.remove(student_num + 1)
    answer = n - len(lost) + len(lend)
    return answer

print(solution(5, [2, 3, 4], [3]))