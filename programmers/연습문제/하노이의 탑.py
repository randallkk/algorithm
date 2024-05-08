import sys

sys.setrecursionlimit = 100000

def solution(n):
    answer = []
    positions = [1] * n
    
    def move(start: int, dest: int, num: int):
        if num == 0: return
        temp = 0
        for i in range(1, 4):
            if i != start and i != dest:
                temp = i
        move(start, temp, num - 1)
        answer.append([start, dest])
        move(temp, dest, num - 1)
        return
    
    move(1, 3, n)
    
    return answer


print(solution(int(input())))

