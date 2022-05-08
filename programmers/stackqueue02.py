def solution1(priorities, location):
    answer = 0
    target = priorities[location]
    pointer = -1
    prior = max(priorities)
    while prior >= target:
        for i in priorities:
            if pointer == len(priorities)-1:
                pointer = 0
            else:
                pointer += 1
            if i == prior:
                priorities[pointer] = -1
                answer += 1
                if pointer == location:
                    return answer
            prior = max(priorities)


    # 매번 max(O(n)) 찾아서 걔 부터 빼기(*n)
    # 걍 9부터 한번씩 다 하기
    # sort 해서 큰 애들 중에 젤 작은애 찾아서...... 이렇게 하면 제일 작은 애 중복 나왔을 때 어딘지 모르잖아.
    # circular linked list 구현...... 전통적인데 위에꺼랑 별 차이 안나잖아...
    # dictionary... index:priority...
    # pointer를 옮기는거로 합의 보기로 했습니다. 
    

if __name__ == '__main__':
    priorities = [1, 1, 9, 1, 1, 1]
    location = 0
    print(solution(priorities, location))