def solution(priorities, location):
    answer = 1
    target = priorities[location]
    later = sorted(priorities[location+1:], reverse=True)
    print(later)
    for i in later:
        if i > target:
            answer += 1
        else:
            break
    for i in priorities[:location]:
        if i >= target:
            answer += 1
    return answer

    # 매번 max(O(n)) 찾아서 걔 부터 빼기(*n)
    # 걍 9부터 한번씩 다 하기
    # sort 해서 큰 애들 중에 젤 작은애 찾아서...... 이렇게 하면 제일 작은 애 중복 나왔을 때 어딘지 모르잖아.
    # circular linked list 구현...... 전통적인데 위에꺼랑 별 차이 안나잖아...
    # dictionary... index:priority...
    

priorities = [2, 1, 3, 2]
location = 2
print(solution(priorities, location))