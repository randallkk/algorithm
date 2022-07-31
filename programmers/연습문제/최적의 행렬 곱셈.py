# 최적의 행렬 곱셈 level 3
# https://school.programmers.co.kr/learn/courses/30/lessons/12942

from collections import deque

def solution(matrix_sizes):
    answer = 0
    
    return answer

# def solution(matrix_sizes):
#     answer = 0
#     sizes = deque([(matrix_sizes[i][1], i+1) for i in range(len(matrix_sizes))])
#     sizes.pop()
#     op_order = sorted(sizes,reverse = True)
#     sizes.appendleft((matrix_sizes[0][0], 0))
#     sizes.append((matrix_sizes[-1][1], len(sizes)))
#     for i in range(len(op_order)):
#         idx = op_order[i][1]
#         left, right = idx-1, idx+1
#         while True:
#             if sizes[left][0] != 0:
#                 break
#             left -= 1
#         while True:
#             if sizes[right][0] != 0:
#                 break
#             right += 1
#         answer += sizes[left][0]*sizes[idx][0]*sizes[right][0]
#         sizes[idx] = (0,idx)

#     return answer

print(solution([[5,3],[3,10],[10,6], [6,2]]))