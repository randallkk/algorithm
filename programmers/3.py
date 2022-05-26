def solution(line):
    answer = []

    characters = [['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],
                  ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P']]
    positions = [(i, j) for i in range(len(characters)) for j in range(len(characters[i]))]
    characters[0].extend(characters[1])
    characters = characters[0]
    left = (1, 0)  # Q
    right = (1, 9)  # P
    for char in line:
        target = positions[characters.index(char)]
        typehand = findhand(target, left, right)
        answer.append(typehand)
        if typehand == 0:
            left = target
        elif typehand == 1:
            right = target
    return answer


def findhand(target, left, right):
    left_keys = ['1', '2', '3', '4', '5', 'Q', 'W', 'E', 'R', 'T']
    left_hori = abs(target[0] - left[0])
    left_vert = abs(target[1] - left[1])
    right_hori = abs(target[0] - right[0])
    right_vert = abs(target[1] - right[1])

    if left_hori + left_vert < right_hori + right_vert:
        return 0
    elif left_hori + left_vert > right_hori + right_vert:
        return 1
    else:
        if left_hori < right_hori:
            return 0
        elif left_hori > right_hori:
            return 1
        else:
            if target in left_keys:
                return 0
            else:
                return 1


print(solution("Q4OYPI"))