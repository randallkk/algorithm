def solution(id_list, report, k):
    answer = []
    report_dict = {}
    for id in id_list:
        report_dict[id] = set()
        answer.append(0)
    for msg in report:
        reporter, reportee = msg.split()
        report_dict[reportee].add(reporter)
    for reporters in report_dict.values():
        if len(reporters) >= k:
            for reporter in reporters:
                answer[id_list.index(reporter)] += 1
    return answer

print(solution(["muzi", "frodo", "apeach", "neo"],["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],2))