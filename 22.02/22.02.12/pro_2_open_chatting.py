def solution(record):
    dic = {}
    result = []
    for re in record:
        command = re.split(' ')
        if command[0] == "Change" or command[0] == "Enter":
            dic[command[1]] = command[2]
    for re in record:
        com = re.split(' ')
        if com[0] == "Enter":
            result.append(dic[com[1]] + "님이 들어왔습니다.")
        elif com[0] == "Leave":
            result.append(dic[com[1]] + "님이 나갔습니다.")
    return result
