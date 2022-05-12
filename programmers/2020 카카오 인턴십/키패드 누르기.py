def solution(numbers, hand):
    answer = ''
    keypad = [1,2,3,4,5,6,7,8,9,-1,0,-1]
    # pos = (idx // 3, idx % 3)
    left_pos = (3,0)
    right_pos = (3,2)
    for num in numbers:
        if num in [1,4,7]:
            idx = keypad.index(num)
            left_pos = (idx // 3, idx % 3)
            answer += 'L'
        elif num in [3,6,9]:
            idx = keypad.index(num)
            right_pos = (idx // 3, idx % 3)
            answer += 'R'
        else:
            idx = keypad.index(num)
            now = (idx // 3, idx % 3)
            left_dist = abs(left_pos[0]-now[0]) + abs(left_pos[1]-now[1])
            right_dist = abs(right_pos[0]-now[0]) + abs(right_pos[1]-now[1])
            if left_dist < right_dist:
                idx = keypad.index(num)
                left_pos = (idx // 3, idx % 3)
                answer += 'L'
            elif left_dist > right_dist:
                idx = keypad.index(num)
                right_pos = (idx // 3, idx % 3)
                answer += 'R'
            else:
                if hand == "right":
                    idx = keypad.index(num)
                    right_pos = (idx // 3, idx % 3)
                    answer += 'R'
                else:
                    idx = keypad.index(num)
                    left_pos = (idx // 3, idx % 3)
                    answer += 'L'
    return answer

print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))