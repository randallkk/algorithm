def solution(lines):
    answer = 0
    timestamps = {}
    for line in lines:
        end = round(convertTimestamp(line.split()[1]), 3)
        cost = float(line.split()[2].rstrip("s"))
        start = round(end - cost + 0.001, 3)
        try:
            timestamps[end] = (timestamps[start][0]+1, timestamps[start][1])
        except KeyError:
            timestamps[start] = (1, 0)
        try:
            timestamps[end] = (timestamps[end][0], timestamps[end][1]+1)
        except KeyError:
            timestamps[end] = (0, 1)
    timestamps = sorted(timestamps.items())

    throughput = 0
    interval = []
    for timestamp in timestamps:
        # 현재 처리 중인 요청 갯수
        throughput += timestamp[1][0] - timestamp[1][1]
        for _ in range(timestamp[1][1]):
            interval.append(timestamp[0])

        # 1초 안에 처리한 로그
        while interval:
            if interval[0] <= timestamp[0] - 1:
                interval.pop(0)
            else:
                break
        if answer < throughput + len(interval):
            answer = throughput + len(interval)

    return answer


def convertTimestamp(timestamp):
    timestamp = list(map(float, timestamp.split(":")))
    return timestamp[0] * 3600 + timestamp[1] * 60 + timestamp[2]


print(solution([
    "2016-09-15 20:59:57.421 0.351s",
    "2016-09-15 20:59:58.233 1.181s",
    "2016-09-15 20:59:58.299 0.8s",
    "2016-09-15 20:59:58.688 1.041s",
    "2016-09-15 20:59:59.591 1.412s",
    "2016-09-15 21:00:00.464 1.466s",
    "2016-09-15 21:00:00.741 1.581s",
    "2016-09-15 21:00:00.748 2.31s",
    "2016-09-15 21:00:00.966 0.381s",
    "2016-09-15 21:00:02.066 2.62s"
]))
