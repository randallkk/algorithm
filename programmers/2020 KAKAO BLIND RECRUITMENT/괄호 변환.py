from collections import deque

def solution(p:str) -> str:
    answer = ''
    brackets = deque(1 if bracket == '(' else -1 for bracket in p)
    def recursive(brackets):
        # 1.
        if not brackets: return brackets
        # 2.
        u = deque()
        sum_u = 0
        correct = True
        while brackets:
            bracket = brackets.popleft()
            u.append(bracket)
            sum_u += bracket
            if sum_u == 0:
                v = brackets
                break
            elif sum_u < 0:
                correct = False
        # print("u:", u, "v:", v)
        recursive_v = recursive(v)
        if correct:     # 3. 문자열 u가 "올바른 괄호 문자열"이라면
            brackets = u
            if recursive_v:
                brackets.extend(recursive_v)
            # print("#3. brackets:", brackets)
        else:           #4. 문자열 u가 "올바른 괄호 문자열"이 아니라면
            u.pop()
            u.popleft()
            brackets = deque([1])
            if recursive_v: brackets.extend(recursive_v)
            brackets.append(-1)
            if u: brackets.extend(deque(map(lambda x: x * -1, u)))
            # print("#4. brackets:", brackets)
        # print("recursive:", brackets)
        return brackets
    brackets = recursive(brackets)
    # print("brackets:", brackets)
    answer = ''.join(['(' if bracket == 1 else ')' for bracket in brackets])
    return answer

print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))
