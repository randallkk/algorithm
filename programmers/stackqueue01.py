import math
def solution1(progresses, speeds):
    answer = []
    date = []
    for i in range(len(progresses)):
        date.append(math.ceil((100 - progresses[i]) / speeds[i]))
    deploy = date[0]
    print(date)
    proj = 1
    for i in date[1:]:
        if i <= deploy:
            proj += 1
        else:
            answer.append(proj)
            proj = 1
            deploy = i
            print(i)
            print(deploy)
    answer.append(proj)
    return answer

def solution2(progresses, speeds):
    answer = []
    date = []
    deploy = -1
    proj = 0
    for p,s in zip(progresses, speeds):
        date = math.ceil((100 - p) / s)
        if date <= deploy:
            proj += 1
        else:
            answer.append(proj)
            proj = 1
            deploy = date
    answer.append(proj)
    return answer[1:]

if __name__ == '__main__':
    progresses = [20, 99, 93, 30, 55, 10]
    speeds = [5, 10, 1, 1, 30, 5]
    
    print(solution2(progresses, speeds))