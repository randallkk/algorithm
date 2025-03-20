# 음악프로그램  gold 3
# https://www.acmicpc.net/problem/2623
# 25-03-21  python3 33432 KB	92 ms


def solution():
    N, M = map(int, input().split())
    adj_list = [set() for _ in range(N + 1)]
    for _ in range(M):
        _, *schedule = map(int, input().split())
        for i in range(1, len(schedule)):
            adj_list[schedule[i]].add(schedule[i - 1])
    
    answer = []
    passed = set()
    renewed = True
    while renewed:
        renewed = False
        for i in range(1, N + 1):
            if i in passed or adj_list[i]:
                continue
            answer.append(i)
            passed.add(i)
            renewed = True
            # 노드 i 제거
            for j in range(1, N + 1):
                if not adj_list[j]: continue
                if i in adj_list[j]:
                    adj_list[j].remove(i)

    if len(passed) < N:
        print(0)
    else:
        print('\n'.join(map(str, answer)))

    return

solution()