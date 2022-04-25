"""
9분 소요, 스스로 풂
틀린 부분
1. 4중 for문에서 max+1 해야 좌표 포함됨
"""

def solution(places):
    ans = []
    for place in places:
        people, flag = [], True
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    people.append([i, j])
        for i in range(len(people)):
            for j in range(i + 1, len(people)):
                distance = abs(people[i][0] - people[j][0]) + abs(people[i][1] - people[j][1])
                if distance == 1:
                    flag = False
                    break
                # 파티션 있는지 확인 필요
                elif distance == 2:
                    for k in range(min(people[i][0], people[j][0]), max(people[i][0], people[j][0])+1):
                        for l in range(min(people[i][1], people[j][1]), max(people[i][1], people[j][1])+1):
                            if people[i] != [k, l] and people[j] != [k, l] and place[k][l] == 'O':
                                flag = False
                                break
        ans.append(1 if flag else 0)
    return ans