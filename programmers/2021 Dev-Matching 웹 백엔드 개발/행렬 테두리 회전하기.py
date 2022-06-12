import time
from pprint import pprint

'''
    # 2d array
    start2 = time.time()
    _2Darr = [[i * columns + j + 1 for j in range(columns)] for i in range(rows)]
    for query in queries:
        _2Darr, moved_nums = rotate_2d(_2Darr, query)
        answer.append(min(moved_nums))
    end2 = time.time()
    print("With 2d-array, time costs", end2 - start2, "ms")
'''


def solution(rows, columns, queries):
    answer = []

    # 1d array
    start1 = time.time()
    _1Dqueries = [[(query[0] - 1) * rows + query[1] - 1, (query[0] - 1) * rows + query[3] - 1,
                   (query[2] - 1) * rows + query[1] - 1, (query[2] - 1) * rows + query[3] - 1]
                  for query in queries]
    _1Darr = [i + 1 for i in range(len(rows * columns))]

    for query in _1Dqueries:
        _1Darr, moved_nums = rotate_1d(_1Darr, query)
        answer.append(min(moved_nums))

    end1 = time.time()
    print("With 1d-array, time costs", end1 - start1, "ms")
    pprint([_1Darr[i:i + columns] for i in range(0, len(_1Darr), columns)])

    return answer


def rotate_1d(arr, query):
    x1, y1, x2, y2 = query
    
    return arr


def rotate_2d(arr, query):
    moved_nums = set()
    x1, y1, x2, y2 = [i - 1 for i in query]
    righttop = arr[x1][y2]
    leftbottom = arr[x2][y1]

    moved_nums.add(righttop)
    moved_nums.add(leftbottom)

    if y2 == len(arr[0]):
        moved_nums.add(min(arr[x1][y1:y2]))
        moved_nums.add(min(arr[x2][y1 + 1:]))

        arr[x1][y1 + 1:] = arr[x1][y1:y2]
        arr[x2][y1:y2] = arr[x2][y1 + 1:]
    else:
        moved_nums.add(min(arr[x1][y1:y2]))
        moved_nums.add(min(arr[x2][y1 + 1:y2 + 1]))
        arr[x1][y1 + 1:y2 + 1] = arr[x1][y1:y2]
        arr[x2][y1:y2] = arr[x2][y1 + 1:y2 + 1]

    for i in range(x2 - x1 - 1):
        moved_nums.add(arr[x1 + i + 1][y1])
        moved_nums.add(arr[x2 - i - 1][y2])
        arr[x1 + i][y1] = arr[x1 + i + 1][y1]
        arr[x2 - i][y2] = arr[x2 - i - 1][y2]

    arr[x2 - 1][y1] = leftbottom
    arr[x1 + 1][y2] = righttop

    return arr, moved_nums


print(solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]))
