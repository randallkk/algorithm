def solution(record):
    answer = []
    nicknames = {}
    logs = []
    for log in record:
        log = log.split()
        if log[0] == "Enter":
            nicknames[log[1]] = log[2]
            logs.append((log[0], log[1]))
        elif log[0] == "Leave":
            logs.append((log[0], log[1]))
        elif log[0] == "Change":
            nicknames[log[1]] = log[2]

    for log in logs:
        if log[0] == "Enter":
            msg = nicknames[log[1]] + "님이 들어왔습니다."
            answer.append(msg)
        elif log[0] == "Leave":
            msg = nicknames[log[1]] + "님이 나갔습니다."
            answer.append(msg)
    return answer


print(solution(
    ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]))
