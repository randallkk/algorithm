def solution(rooms, target):
    candid = {}
    for idx in range(len(rooms)):
        room_num = find_roomno(rooms[idx])
        for person in ppl_in_room(rooms[idx]):
            if person not in candid:
                candid[person] = [[room_num], abs(room_num - target)]
            else:
                candid[person][0].append(room_num)
                if candid[person][1] > abs(room_num - target):
                    candid[person][1] = abs(room_num - target)
    print(candid)
    priorities = sorted(candid.items(), key=lambda item: (len(item[1][0]), item[1][1], item[0]))
    answer = [prior[0] for prior in priorities if prior[1][1]]
    return answer


def ppl_in_room(room):
    people = room.split(']')[1].split(',')
    return people


def find_roomno(room):
    room_num = room.split('[')[1].split(']')[0]
    return int(room_num)


print(solution(["[403]James", "[404]Azad,Louis,Andy,James", "[101]Azad,Guard"], 403))
